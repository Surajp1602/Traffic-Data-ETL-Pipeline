-- Average vehicles by location

SELECT
location,
AVG(vehicle_count)
FROM traffic_data
GROUP BY location;

-- Peak traffic

SELECT
location,
MAX(vehicle_count)
FROM traffic_data
GROUP BY location;

-- Average speed

SELECT
location,
AVG(avg_speed)
FROM traffic_data
GROUP BY location;

-- Hourly traffic trend

SELECT
hour,
AVG(vehicle_count)
FROM traffic_data
GROUP BY hour;