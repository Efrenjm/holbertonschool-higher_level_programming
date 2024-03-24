-- lists all the cities of California in the htbn_0d_usa database
SELECT * FROM cities
WHERE cities.state_id = (
    SELECT id FROM states WHERE cities.name LIKE 'California'
    )
ORDER BY cities.id;