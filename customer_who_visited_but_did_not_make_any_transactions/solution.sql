SELECT customer_id, 
       SUM(
        CASE WHEN t.transaction_id IS NULL 
        THEN 1 ELSE 0 END
       ) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t 
    ON t.visit_id = v.visit_id
GROUP BY v.customer_id
HAVING count_no_trans > 0;

-- OR 

SELECT customer_id, 
       COUNT(v.visit_id) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t 
    ON t.visit_id = v.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id