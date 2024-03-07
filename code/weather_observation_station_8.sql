/* https://www.hackerrank.com/challenges/weather-observation-station-8/problem */
select distinct(city) from station
where
    left(city, 1) in ('a', 'e', 'i', 'o', 'u')
    and
    right(city, 1) in ('a', 'e', 'i', 'o', 'u');
