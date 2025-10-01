SELECT name, cuisine, avg_cost
FROM restaurants
ORDER BY avg_cost ASC
LIMIT 5;


SELECT name, cuisine, distance_miles, rating
FROM restaurants
WHERE distance_miles <= 5 AND rating >= 4.0
ORDER BY rating DESC, distance_miles ASC;

-- exercise 1
SELECT name, cuisine, distance_miles
FROM restaurants
WHERE distance_miles <= 2
ORDER BY distance_miles ASC;

