use test;

drop table if not exists users;

CREATE TABLE if not exists users
(
id int,
username varchar(40),
lastname varchar(60),
age tinyint,
index(username)
);

insert into users values
(5, 'Anton', 'Neizvestny', '18'),
(3, 'Artem', 'Vernikov', '20'),
(5, 'Dmitrii', 'Odintsev', '21'),
(5, 'Vika', 'Evseeva', '19');

update users set id = 4 where username = 'Vika';

select * FROM users;

--Проверка индекса
describe users;