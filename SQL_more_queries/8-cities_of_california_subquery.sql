-- lists all the cities of California in the htbn_0d_usa database
SELECT cities.id, cities.name FROM cities
WHERE state_id = (
      SELECT id FROM states WHERE name = 'California'
)
ORDER BY cities.id;