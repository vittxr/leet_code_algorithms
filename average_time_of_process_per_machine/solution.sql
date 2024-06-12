SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM Activity as a
JOIN Activity as a1 
    ON a1.machine_id = a.machine_id AND
       a1.process_id = a.process_id AND
       a1.activity_type = 'start'
JOIN Activity as a2
    ON a2.machine_id = a.machine_id AND
       a2.process_id = a.process_id AND
       a2.activity_type = 'end'
GROUP BY a.machine_id;