-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:8889
-- Время создания: Окт 27 2026 г., 16:14
-- Версия сервера: 8.0.44
-- Версия PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `sever_ural`
--

-- --------------------------------------------------------

--
-- Структура таблицы `administrator`
--

CREATE TABLE `administrator` (
  `id` int NOT NULL COMMENT 'PK',
  `login` varchar(50) NOT NULL COMMENT 'Логин администратора',
  `password` varchar(100) NOT NULL COMMENT 'Пароль администратора',
  `email` varchar(100) NOT NULL COMMENT 'Почта администратора'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Таблица администратора';

--
-- Дамп данных таблицы `administrator`
--

INSERT INTO `administrator` (`id`, `login`, `password`, `email`) VALUES
(1, 'admin', 'admin1', 'ivanov@sever-tour.ru'),
(2, 'admin_petrova', 'petrova_2024', 'petrova@sever-tour.ru'),
(3, 'admin_smirnov', 'smirnov_2024', 'smirnov@sever-tour.ru'),
(4, 'admin_kuznec', 'kuznec_2024', 'kuznecov@sever-tour.ru'),
(5, 'admin_volkov', 'volkov_2024', 'volkov@sever-tour.ru');

-- --------------------------------------------------------

--
-- Структура таблицы `booking`
--

CREATE TABLE `booking` (
  `id` int NOT NULL COMMENT 'PK',
  `booking_date` datetime NOT NULL COMMENT 'Дата бронирования',
  `status` enum('Активен','Неактивен') NOT NULL COMMENT 'Статус бронирования',
  `people_count` int NOT NULL COMMENT 'Количество человек',
  `tour_id` int NOT NULL COMMENT 'FK',
  `tourist_id` int NOT NULL COMMENT 'FK',
  `admin_id` int NOT NULL COMMENT 'FK',
  `guide_id` int NOT NULL COMMENT 'FK'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Таблица бронирования';

--
-- Дамп данных таблицы `booking`
--

INSERT INTO `booking` (`id`, `booking_date`, `status`, `people_count`, `tour_id`, `tourist_id`, `admin_id`, `guide_id`) VALUES
(1, '2026-05-01 10:15:00', 'Активен', 2, 1, 1, 1, 1),
(2, '2026-05-10 14:30:00', 'Активен', 3, 1, 2, 1, 1),
(3, '2026-06-01 09:00:00', 'Активен', 1, 2, 3, 2, 2),
(4, '2026-07-05 16:45:00', 'Активен', 4, 3, 4, 3, 3),
(5, '2026-08-01 11:20:00', 'Неактивен', 2, 5, 5, 1, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `equipment`
--

CREATE TABLE `equipment` (
  `id` int NOT NULL COMMENT 'PK',
  `name` varchar(100) NOT NULL COMMENT 'Название снаряжения',
  `category` enum('Личное','Бивачное','Общегрупповое','Специальное') NOT NULL COMMENT 'Категория снаряжения'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Таблица снаряжения';

--
-- Дамп данных таблицы `equipment`
--

INSERT INTO `equipment` (`id`, `name`, `category`) VALUES
(1, 'Палатка 3-местная', 'Бивачное'),
(2, 'Спальник зимний -25°C', 'Личное'),
(3, 'Котелок 5л', 'Общегрупповое'),
(4, 'Ледоруб', 'Специальное'),
(5, 'Аптечка групповая', 'Общегрупповое');

-- --------------------------------------------------------

--
-- Структура таблицы `guest`
--

CREATE TABLE `guest` (
  `id` int NOT NULL COMMENT 'PK',
  `visit_date` datetime NOT NULL COMMENT 'Дата визита гостя'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Таблица гостя';

--
-- Дамп данных таблицы `guest`
--

INSERT INTO `guest` (`id`, `visit_date`) VALUES
(1, '2026-09-01 12:00:00'),
(2, '2026-09-05 15:30:00'),
(3, '2026-09-10 09:45:00'),
(4, '2026-09-14 18:20:00'),
(5, '2026-09-17 20:10:00');

-- --------------------------------------------------------

--
-- Структура таблицы `guest_guide_view`
--

CREATE TABLE `guest_guide_view` (
  `guest_id` int NOT NULL COMMENT 'FK',
  `guide_id` int NOT NULL COMMENT 'FK'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Таблица связи Гость-Гид';

--
-- Дамп данных таблицы `guest_guide_view`
--

INSERT INTO `guest_guide_view` (`guest_id`, `guide_id`) VALUES
(1, 1),
(1, 2),
(2, 1),
(3, 5),
(4, 3),
(4, 5),
(5, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `guest_tour_view`
--

CREATE TABLE `guest_tour_view` (
  `guest_id` int NOT NULL COMMENT 'FK',
  `tour_id` int NOT NULL COMMENT 'FK'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Таблица связи Гость-Тур';

--
-- Дамп данных таблицы `guest_tour_view`
--

INSERT INTO `guest_tour_view` (`guest_id`, `tour_id`) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 4),
(3, 5),
(4, 2),
(4, 3),
(4, 4),
(5, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `guide`
--

CREATE TABLE `guide` (
  `id` int NOT NULL COMMENT 'PK',
  `first_name` varchar(100) NOT NULL COMMENT 'Имя гида',
  `last_name` varchar(100) NOT NULL COMMENT 'Фамилия гида',
  `phone` varchar(20) NOT NULL COMMENT 'Телефон гида',
  `email` varchar(100) NOT NULL COMMENT 'Почта гида',
  `login` varchar(50) NOT NULL COMMENT 'Логин гида',
  `password` varchar(100) NOT NULL COMMENT 'Пароль гида',
  `qualification` enum('Экскурсовод','Гид-переводчик','Инструктор-проводник') NOT NULL COMMENT 'Квалификация гида',
  `rating` decimal(3,2) NOT NULL COMMENT 'Рейтинг гида',
  `status` enum('Активен','Неактивен') NOT NULL COMMENT 'Статус гида',
  `admin_id` int NOT NULL COMMENT 'FK',
  `tourist_id` int NOT NULL COMMENT 'FK'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Таблица гида';

--
-- Дамп данных таблицы `guide`
--

INSERT INTO `guide` (`id`, `first_name`, `last_name`, `phone`, `email`, `login`, `password`, `qualification`, `rating`, `status`, `admin_id`, `tourist_id`) VALUES
(1, 'Виктор', 'Мельник', '+79211111101', 'melnik@sever-tour.ru', 'guide', 'guide1', 'Инструктор-проводник', 4.85, 'Активен', 1, 1),
(2, 'Ольга', 'Крылова', '+79211111102', 'krylova@sever-tour.ru', 'krylova_o', 'g02', 'Гид-переводчик', 4.60, 'Активен', 1, 2),
(3, 'Сергей', 'Горный', '+79211111103', 'gorny@sever-tour.ru', 'gorny_s', 'g03', 'Инструктор-проводник', 4.95, 'Активен', 2, 3),
(4, 'Анна', 'Северова', '+79211111104', 'severova@sever-tour.ru', 'severova_a', 'g04', 'Экскурсовод', 4.30, 'Неактивен', 2, 4),
(5, 'Игорь', 'Тайгин', '+79211111105', 'taigin@sever-tour.ru', 'taigin_i', 'g05', 'Инструктор-проводник', 4.75, 'Активен', 3, 5);

-- --------------------------------------------------------

--
-- Структура таблицы `review`
--

CREATE TABLE `review` (
  `id` int NOT NULL COMMENT 'PK',
  `rating` enum('1','2','3','4','5') NOT NULL COMMENT 'Оценка',
  `comment` text NOT NULL COMMENT 'Комментарий отзыва',
  `review_date` date NOT NULL COMMENT 'Дата отзыва',
  `tourist_id` int NOT NULL COMMENT 'FK',
  `tour_id` int NOT NULL COMMENT 'FK',
  `admin_id` int NOT NULL COMMENT 'FK',
  `guide_id` int NOT NULL COMMENT 'FK'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Таблица отзыва';

--
-- Дамп данных таблицы `review`
--

INSERT INTO `review` (`id`, `rating`, `comment`, `review_date`, `tourist_id`, `tour_id`, `admin_id`, `guide_id`) VALUES
(1, '5', 'Незабываемое восхождение! Гид Виктор — профессионал.', '2026-06-25', 1, 1, 1, 1),
(2, '4', 'Красивая природа, но погода подвела. Всё понравилось.', '2026-07-10', 2, 2, 1, 2),
(3, '5', 'Сплав по Вишере — лучший отдых в жизни!', '2026-07-25', 3, 3, 2, 3),
(4, '3', 'Маршрут сложный, но интересный. Снаряжение частично старое.', '2026-08-15', 4, 4, 3, 5),
(5, '5', 'Экспедиция Ивдель–Оус — настоящий Северный Урал!', '2026-09-15', 5, 5, 1, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `route`
--

CREATE TABLE `route` (
  `id` int NOT NULL COMMENT 'PK',
  `name` varchar(255) NOT NULL COMMENT 'Название маршрута',
  `type` enum('Линейный','Радиальный','Кольцевой') NOT NULL COMMENT 'Тип маршрута',
  `difficulty` enum('Низкая','Средняя','Высокая','Очень высокая') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'Сложность маршрута',
  `length_km` decimal(6,2) NOT NULL COMMENT 'Протяженность маршрута'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Таблица маршрута';

--
-- Дамп данных таблицы `route`
--

INSERT INTO `route` (`id`, `name`, `type`, `difficulty`, `length_km`) VALUES
(1, 'Восхождение на Конжаковский Камень', 'Радиальный', 'Высокая', 42.50),
(2, 'Денежкин Камень: тропа заповедника', 'Кольцевой', 'Средняя', 38.00),
(3, 'Сплав по реке Вишера', 'Линейный', 'Низкая', 95.00),
(4, 'Хребет Кваркуш: Карстовые озера', 'Кольцевой', 'Средняя', 60.00),
(5, 'Тропа Северного Урала: Ивдель–Оус', 'Линейный', 'Очень высокая', 120.00);

-- --------------------------------------------------------

--
-- Структура таблицы `tour`
--

CREATE TABLE `tour` (
  `id` int NOT NULL COMMENT 'PK',
  `name` varchar(100) NOT NULL COMMENT 'Название тура',
  `status` enum('Активен','Неактивен') NOT NULL COMMENT 'Статус тура',
  `total_seats` int NOT NULL COMMENT 'Количество мест',
  `start_date` date NOT NULL COMMENT 'Дата начала',
  `end_date` date NOT NULL COMMENT 'Дата окончания',
  `route_id` int NOT NULL COMMENT 'FK',
  `guide_id` int NOT NULL COMMENT 'FK',
  `admin_id` int NOT NULL COMMENT 'FK',
  `tourist_id` int NOT NULL COMMENT 'FK'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Таблица тура';

--
-- Дамп данных таблицы `tour`
--

INSERT INTO `tour` (`id`, `name`, `status`, `total_seats`, `start_date`, `end_date`, `route_id`, `guide_id`, `admin_id`, `tourist_id`) VALUES
(1, 'Восхождение на Конжак (7 дней)', 'Активен', 12, '2026-06-15', '2026-06-21', 1, 1, 1, 1),
(2, 'Заповедник Денежкин Камень (5 дней)', 'Активен', 10, '2026-07-01', '2026-07-05', 2, 2, 1, 2),
(3, 'Сплав по Вишере (4 дня)', 'Активен', 15, '2026-07-20', '2026-07-23', 3, 3, 2, 3),
(4, 'Кваркуш: озёра и карсты (6 дней)', 'Активен', 8, '2026-08-05', '2026-08-10', 4, 5, 3, 4),
(5, 'Тропа Ивдель–Оус: экспедиция (10 дней)', 'Неактивен', 6, '2026-09-01', '2026-09-10', 5, 1, 1, 5);

-- --------------------------------------------------------

--
-- Структура таблицы `tourist`
--

CREATE TABLE `tourist` (
  `id` int NOT NULL COMMENT 'PK',
  `first_name` varchar(100) NOT NULL COMMENT 'Имя туриста',
  `last_name` varchar(100) NOT NULL COMMENT 'Фамилия туриста',
  `phone` varchar(20) NOT NULL COMMENT 'Телефон туриста',
  `email` varchar(100) NOT NULL COMMENT 'Почта туриста',
  `login` varchar(50) NOT NULL COMMENT 'Логин туриста',
  `password` varchar(100) NOT NULL COMMENT 'Пароль туриста',
  `admin_id` int NOT NULL COMMENT 'FK'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Таблица туриста';

--
-- Дамп данных таблицы `tourist`
--

INSERT INTO `tourist` (`id`, `first_name`, `last_name`, `phone`, `email`, `login`, `password`, `admin_id`) VALUES
(1, 'Алексей', 'Сидоров', '+79123456701', 'sidorov@mail.ru', 'tourist', 'tourist1', 1),
(2, 'Мария', 'Иванова', '+79123456702', 'ivanova@mail.ru', 'ivanova_m', '12346', 1),
(3, 'Дмитрий', 'Петров', '+79123456703', 'petrov@mail.ru', 'petrov_d', '12347', 2),
(4, 'Екатерина', 'Смирнова', '+79123456704', 'smirnova@mail.ru', 'smirnova_e', '12348', 2),
(5, 'Николай', 'Орлов', '+79123456705', 'orlov@mail.ru', 'orlov_n', '12349', 3);

-- --------------------------------------------------------

--
-- Структура таблицы `tour_equipment`
--

CREATE TABLE `tour_equipment` (
  `tour_id` int NOT NULL COMMENT 'FK',
  `equipment_id` int NOT NULL COMMENT 'FK'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Таблица связи Тур-Снаряжение';

--
-- Дамп данных таблицы `tour_equipment`
--

INSERT INTO `tour_equipment` (`tour_id`, `equipment_id`) VALUES
(1, 1),
(1, 2),
(1, 4),
(1, 5),
(2, 1),
(2, 2),
(2, 5),
(3, 1),
(3, 2),
(3, 3),
(4, 1),
(4, 2),
(4, 5),
(5, 1),
(5, 2),
(5, 3),
(5, 4),
(5, 5);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `administrator`
--
ALTER TABLE `administrator`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tour_id` (`tour_id`),
  ADD KEY `tourist_id` (`tourist_id`),
  ADD KEY `admin_id` (`admin_id`),
  ADD KEY `guide_id` (`guide_id`);

--
-- Индексы таблицы `equipment`
--
ALTER TABLE `equipment`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `guest`
--
ALTER TABLE `guest`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `guest_guide_view`
--
ALTER TABLE `guest_guide_view`
  ADD KEY `guest_id` (`guest_id`),
  ADD KEY `guide_id` (`guide_id`);

--
-- Индексы таблицы `guest_tour_view`
--
ALTER TABLE `guest_tour_view`
  ADD KEY `guest_id` (`guest_id`),
  ADD KEY `tour_id` (`tour_id`);

--
-- Индексы таблицы `guide`
--
ALTER TABLE `guide`
  ADD PRIMARY KEY (`id`),
  ADD KEY `admin_id` (`admin_id`),
  ADD KEY `tourist_id` (`tourist_id`);

--
-- Индексы таблицы `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tourist_id` (`tourist_id`),
  ADD KEY `tour_id` (`tour_id`),
  ADD KEY `admin_id` (`admin_id`),
  ADD KEY `guide_id` (`guide_id`);

--
-- Индексы таблицы `route`
--
ALTER TABLE `route`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `tour`
--
ALTER TABLE `tour`
  ADD PRIMARY KEY (`id`),
  ADD KEY `route_id` (`route_id`),
  ADD KEY `guide_id` (`guide_id`),
  ADD KEY `admin_id` (`admin_id`),
  ADD KEY `tourist_id` (`tourist_id`);

--
-- Индексы таблицы `tourist`
--
ALTER TABLE `tourist`
  ADD PRIMARY KEY (`id`),
  ADD KEY `admin_id` (`admin_id`);

--
-- Индексы таблицы `tour_equipment`
--
ALTER TABLE `tour_equipment`
  ADD KEY `tour_id` (`tour_id`),
  ADD KEY `equipment_id` (`equipment_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `administrator`
--
ALTER TABLE `administrator`
  MODIFY `id` int NOT NULL AUTO_INCREMENT COMMENT 'PK', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `booking`
--
ALTER TABLE `booking`
  MODIFY `id` int NOT NULL AUTO_INCREMENT COMMENT 'PK', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `equipment`
--
ALTER TABLE `equipment`
  MODIFY `id` int NOT NULL AUTO_INCREMENT COMMENT 'PK', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `guest`
--
ALTER TABLE `guest`
  MODIFY `id` int NOT NULL AUTO_INCREMENT COMMENT 'PK', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `guide`
--
ALTER TABLE `guide`
  MODIFY `id` int NOT NULL AUTO_INCREMENT COMMENT 'PK', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `review`
--
ALTER TABLE `review`
  MODIFY `id` int NOT NULL AUTO_INCREMENT COMMENT 'PK', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `route`
--
ALTER TABLE `route`
  MODIFY `id` int NOT NULL AUTO_INCREMENT COMMENT 'PK', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `tour`
--
ALTER TABLE `tour`
  MODIFY `id` int NOT NULL AUTO_INCREMENT COMMENT 'PK', AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `tourist`
--
ALTER TABLE `tourist`
  MODIFY `id` int NOT NULL AUTO_INCREMENT COMMENT 'PK', AUTO_INCREMENT=6;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`tour_id`) REFERENCES `tour` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`tourist_id`) REFERENCES `tourist` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`admin_id`) REFERENCES `administrator` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `booking_ibfk_4` FOREIGN KEY (`guide_id`) REFERENCES `guide` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `guest_guide_view`
--
ALTER TABLE `guest_guide_view`
  ADD CONSTRAINT `guest_guide_view_ibfk_1` FOREIGN KEY (`guest_id`) REFERENCES `guest` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `guest_guide_view_ibfk_2` FOREIGN KEY (`guide_id`) REFERENCES `guide` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `guest_tour_view`
--
ALTER TABLE `guest_tour_view`
  ADD CONSTRAINT `guest_tour_view_ibfk_1` FOREIGN KEY (`tour_id`) REFERENCES `tour` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `guest_tour_view_ibfk_2` FOREIGN KEY (`guest_id`) REFERENCES `guest` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `guide`
--
ALTER TABLE `guide`
  ADD CONSTRAINT `guide_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `administrator` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `guide_ibfk_2` FOREIGN KEY (`tourist_id`) REFERENCES `tourist` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `review`
--
ALTER TABLE `review`
  ADD CONSTRAINT `review_ibfk_1` FOREIGN KEY (`tourist_id`) REFERENCES `tourist` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `review_ibfk_2` FOREIGN KEY (`tour_id`) REFERENCES `tour` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `review_ibfk_3` FOREIGN KEY (`admin_id`) REFERENCES `administrator` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `review_ibfk_4` FOREIGN KEY (`guide_id`) REFERENCES `guide` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `tour`
--
ALTER TABLE `tour`
  ADD CONSTRAINT `tour_ibfk_1` FOREIGN KEY (`route_id`) REFERENCES `route` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tour_ibfk_2` FOREIGN KEY (`guide_id`) REFERENCES `guide` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tour_ibfk_3` FOREIGN KEY (`admin_id`) REFERENCES `administrator` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tour_ibfk_4` FOREIGN KEY (`tourist_id`) REFERENCES `tourist` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `tourist`
--
ALTER TABLE `tourist`
  ADD CONSTRAINT `tourist_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `administrator` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `tour_equipment`
--
ALTER TABLE `tour_equipment`
  ADD CONSTRAINT `tour_equipment_ibfk_1` FOREIGN KEY (`tour_id`) REFERENCES `tour` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tour_equipment_ibfk_2` FOREIGN KEY (`equipment_id`) REFERENCES `equipment` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
