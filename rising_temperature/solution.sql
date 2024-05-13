SELECT id 
FROM (
    SELECT id, 
           temperature, 
           recordDate,
           LAG(temperature, 1) OVER (ORDER BY recordDate) AS prevTemp,
           LAG(recordDate, 1) OVER (ORDER BY recordDate) AS prevRecordDt
    FROM Weather
) AS temp_comparison
WHERE temperature > prevTemp AND timestampdiff(DAY, prevRecordDt, recordDate) = 1;