# Write your MySQL query statement below
select Email  from Person 
GROUP BY email
HAVING COUNT(*) > 1