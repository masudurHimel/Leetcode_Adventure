# Write your MySQL query statement below
select empU.unique_id, emp.name
from Employees as emp
left join EmployeeUNI as empU
on emp.id = empU.id