import pymysql

def get_db_connection():
    return pymysql.connect(
        host = 'localhost',
        port = 8889,
        user = 'root',
        password = 'root',
        database = 'sever_ural'
    )

def get_active_tours(limit=5):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    t.id,
                    t.name,
                    CONCAT(g.first_name, ' ', g.last_name) AS guide_name
                FROM tour t
                JOIN guide g ON t.guide_id = g.id
                WHERE t.status = 'Активен'
                ORDER BY t.start_date
                LIMIT %s
            """, (limit,))
            return cursor.fetchall()
    except Exception as e:
        print(f"Ошибка БД при получении туров: {e}")
        return []
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()

def get_active_guides(limit=4, exclude_id=None):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = """
                SELECT 
                    g.id,
                    CONCAT(g.first_name, ' ', g.last_name) AS full_name,
                    g.qualification,
                    COUNT(t.id) AS active_tours
                FROM guide g
                LEFT JOIN tour t 
                    ON t.guide_id = g.id AND t.status = 'Активен'
                WHERE g.status = 'Активен'
            """
            params = []
            if exclude_id is not None:
                sql += " AND g.id != %s"
                params.append(exclude_id)
            sql += """
                GROUP BY g.id, g.first_name, g.last_name, g.qualification
                ORDER BY g.rating DESC
                LIMIT %s
            """
            params.append(limit)
            cursor.execute(sql, params)
            return cursor.fetchall()
    except Exception as e:
        print(f"Ошибка БД при получении гидов: {e}")
        return []
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()

def get_guide_profile(guide_id):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    first_name, last_name, phone, email,
                    login, qualification, rating, status
                FROM guide
                WHERE id = %s
            """, (guide_id,))
            return cursor.fetchone()
    except Exception as e:
        print(f"Ошибка БД при получении профиля гида: {e}")
        return None
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()

def get_reviews(limit=4):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    r.id,
                    r.rating,
                    r.comment,
                    r.review_date,
                    CONCAT(t.first_name, ' ', t.last_name) AS tourist_name,
                    tr.name AS tour_name,
                    CONCAT(g.first_name, ' ', g.last_name) AS guide_name
                FROM review r
                JOIN tourist t  ON r.tourist_id = t.id
                JOIN tour tr    ON r.tour_id    = tr.id
                JOIN guide g    ON r.guide_id   = g.id
                ORDER BY r.review_date DESC
                LIMIT %s
            """, (limit,))
            return cursor.fetchall()
    except Exception as e:
        print(f"Ошибка БД при получении отзывов: {e}")
        return []
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()


def get_review_by_id(review_id):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    r.id,
                    r.rating,
                    r.comment,
                    r.review_date,
                    CONCAT(t.first_name, ' ', t.last_name) AS tourist_name,
                    tr.name AS tour_name,
                    CONCAT(g.first_name, ' ', g.last_name) AS guide_name
                FROM review r
                JOIN tourist t  ON r.tourist_id = t.id
                JOIN tour tr    ON r.tour_id    = tr.id
                JOIN guide g    ON r.guide_id   = g.id
                WHERE r.id = %s
            """, (review_id,))
            return cursor.fetchone()
    except Exception as e:
        print(f"Ошибка БД: {e}")
        return None
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()

def get_tour_by_id(tour_id):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    id,
                    name,
                    status,
                    total_seats,
                    start_date,
                    end_date
                FROM tour
                WHERE id = %s
            """, (tour_id,))
            return cursor.fetchone()
    except Exception as e:
        print(f"Ошибка БД при получении тура: {e}")
        return None
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()