-- Display only the people wich the score is greater than 10, decreasing.
SELECT `score`, `name` FROM `second_table`
WHERE score >= 10
ORDER BY `score` DESC;
