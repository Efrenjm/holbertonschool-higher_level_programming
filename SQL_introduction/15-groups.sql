-- Gets the number of students with the same score
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;