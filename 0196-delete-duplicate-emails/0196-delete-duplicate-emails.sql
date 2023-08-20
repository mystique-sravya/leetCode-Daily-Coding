# Write your MySQL query statement below
delete ep from Person ep inner join Person p on ep.email = p.email and ep.id > p.id ;