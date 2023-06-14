# Write your MySQL query statement below
select x.id
from Weather as x, Weather as y
where x.temperature > y.temperature and DATEDIFF(x.recordDate, y.recordDate)=1