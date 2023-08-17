-- sty  3 cities with  highest average
-- temperaturs between July and August.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;s all cities contained in the database hbtn_0d_usa
