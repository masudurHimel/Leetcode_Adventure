# Write your MySQL query statement below
select machine_id, ROUND(SUM(CASE WHEN activity_type = "end" THEN timestamp ELSE -timestamp END) / Count(distinct process_id), 3) as processing_time
from Activity
group by machine_id