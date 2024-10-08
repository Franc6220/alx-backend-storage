-- SQL script that lists all bands with Glam rock as their main style,
-- ranked by their longevity
SELECT `band_name`,
       IFNULL(2022 - `formed`, 0) AS `lifespan`
FROM `metal_bands`
WHERE FIND_IN_SET('Glam rock', `style`)
ORDER BY `lifespan` DESC;

