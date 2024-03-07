/* https://www.hackerrank.com/challenges/weather-observation-station-11/problem */
select distinct(city) from station
where
    left(city, 1) not in ('a', 'e', 'i', 'o', 'u')
    or
    right(city, 1) not in ('a', 'e', 'i', 'o', 'u');
