-- SELECT name FROM Customer
-- WHERE NOT referee_id <=> 2;

-- following solution is faster.
SELECT name FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;