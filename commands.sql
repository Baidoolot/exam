SELECT * FROM developers WHERE date > 1995 AND sex = 'male';

SELECT name, lastname FROM developers 
UNION
SELECT name, lastname FROM project_managers;

SELECT * FROM developers WHERE date > 1995;

SELECT name FROM developers WHERE sex = 'female'
UNION
SELECT COUNT(sex) FROM developers WHERE sex = 'female';

SELECT COUNT(sex) FROM developers WHERE sex ='male';

SELECT COUNT(*) FROM developers;
