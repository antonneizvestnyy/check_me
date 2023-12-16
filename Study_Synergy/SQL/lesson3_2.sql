/*

Задание:
Для БД из прошлого домашнего задания (8). 
В таблицу "Пользователи" вставить 5 записей с датой регистрации в сентябре
2009 года, но разные дни. Пример:
1 пользователь: 09.09.2009
2 пользователь: 15.09.2009
3 пользователь: 17.09.2009
4 пользователь: 01.09.2009
5 пользователь: 25.09.2009

В таблицы "Сериалы", "Отзывы", "Жанры" вставить по 5 любых записей.
При вставке новых записей показать несколько способов: 
- вставка всех полей вручную
- вставка только некоторых полей (поля выбрать самостоятельно).

В таблице "Пользователи" обновить:
1. Отображаемое имя всех пользователей на "пользователь"
2. Фамилию пользователя с датой регистрации 09.09.2009 на "Сенаторов"

В таблице "Жанры" удалить запись с жанром на выбор студента
(показать 2 варианта удаления: 
- по идентификатору
- по названию.
Один из вариантов закомментировать)

*/


create DATABASE users;
use users;


drop table users;

CREATE TABLE IF NOT EXISTS users
(
id int,
username varchar(30),
lastname varchar(40),
email varchar(50),
password_hash varchar(60),
`reg data` varchar(30),
index(username, email)
);


insert into users values
(1, 'Артем', 'Тимофеев', 'schumacher_a@mail.ru', '18345345', '13.09.2009' ),
(2, 'Николай', 'Евсеев', 'evseev_k@mail.ru','21231230', '22.09.2009' ),
(3, 'Антон', 'Неизвестный', 'aneizvestny@mail.ru', '2423421897', '11.09.2009' ),
(4, 'Виктория', 'Кравцева', 'viktoria2003@mail.ru', '1234321239', '08.09.2009' ),
(5, 'Алексей', 'Бегунов', 'a_begunov@mail.ru','86756719', '15.09.2009' );

select * FROM users;


CREATE TABLE if not exists serials
(
id int,
name varchar(30),
authors varchar(40),
`short description` text,
`publish year` date,
index(name, authors)
);


-- В ручную все поля
insert into serials values
(1, 'Хороший доктор', 'Девид Шор', 'Это захватывающая медицинская драма, которая рассказывает историю про Доктора Шона Мерфи', '25.09.2017' ),
(2, 'Скорпион', 'Сэм Хилл', 'Oснованный на жизни и деятельности гения и компьютерного эксперта Уолтера О’Брайана.', '22.09.2014' ),
(3, 'Доктор Хаус', 'Девид Шор', 'О выдающемся враче-диагносте Грегори Хаусе и его команде. ', '21.05.2012' ),
(4, 'Теория большого взрыва', 'Чак Лорри', 'Главными героями сериала являются молодые физики Леонард Хофстедтер и Шелдон Купер — типичные представители гик-культуры. ', '24.09.2007' );
--(5, 'Шерлок Холмс', 'Марк Гэтисс', 'Британский сериал в жанре детективной криминальной драмы', '25.07.2010' );


select * FROM serials;

/*
Поля на выбор

insert into serials (name, authors) values ('Доктор Хаус', 'Девид Шор');
insert into serials (id, name, authors,`short description`) values (5, 'Шерлок Холмс', 'Марк Гэтисс', 'британский сериал в жанре детективной криминальной драмы');

*/


CREATE TABLE if not exists genre
(
id int,
name_genre varchar(30),
index(name_genre)
);

--В ручную все поля

insert into genre values
--(1, 'комедия'),
(2, 'ужасы'),
--(3, 'детектив'),
--(4, 'драмма'),
(5, 'приключие');


/*

Поля на выбор

insert into genre (name_genre) values
('комедия'),
('детектив'),
('драмма');

*/

SELECT * from genre;

drop table reviews;

CREATE TABLE if not exists reviews
(
id int,
name varchar(30),
comment text,
`add year` varchar(20),
index(name)
);

SELECT * from reviews;

-- в ручную все поля
insert into reviews values
(1, 'Антон', 'очень интересно', '3.11.2015' ),
(2, 'Тима', 'интересно', '03.10.2022' ),
(3, 'Дмитрий', 'на 1 раз', '12.11.2009' ),
(4, 'Николай', 'советую!', '01.10.2019' ),
(5, 'Наталья', 'скучно', '20.11.2014' );

/*

Поля на выбор

insert into reviews (name, comment) values
('Антон', 'очень интересно' ),
('Тима', 'интересно'),
('Дмитрий', 'на 1 раз');

*/

--1. Отображаемое имя всех пользователей на "пользователь"
--глобальное обновление имени пользователей.

UPDATE users set username  = "Пользователь";
select * from users;

-- 2. Фамилию пользователя с датой регистрации 09.09.2009 на "Сенаторов"
-- Измненение для конкретного пользовеля.

UPDATE users set lastname = "Сенаторов" where `reg data` = "8.09.2009";
select * from users;


-- удаление по идентификатору в тиблице жанры

delete from genre where id = 2;
SELECT * from genre;

-- удаление по названию в таблице жанры

-- delete from genre where name_genre = 'драмма';
-- SELECT * from genre;Bbelo4ka3
