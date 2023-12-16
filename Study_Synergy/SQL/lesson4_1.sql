
/*

-----Выборка данных-------
where
where * * in ()
where * * between - между (годом)
=>
<
>
<=
!=
=
and
or
like ' value' шаблоны '%'- сколько угодно символов, '_'  - 1 буква  ,
если'\_o%' , '\%%' то нужно указать символ - \


-------Переименование полей--------
as

----select-----
select * from db limit ' 2000'

---sort----
order by 'model', 'vin'; - несколько сортировок

Example:

select make, model from autos
where drive_wheels in ('awd', '4wd')
order by model, cylinder_layout
limit 10


*/