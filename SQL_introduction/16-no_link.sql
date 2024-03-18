-- updates the score of Bob to 10
SELECT score, name 
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;