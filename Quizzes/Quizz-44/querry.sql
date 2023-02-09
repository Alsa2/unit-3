-- SQLite

-- List all tables in the database
SELECT name FROM sqlite_master WHERE type='table';

-- Get Friendly and male inhabitants
SELECT * FROM INHABITANT WHERE gender = "Male" AND state = 'Friendly';

-- What is the average gold of all inhabitants in village 1?
SELECT AVG(gold) FROM INHABITANT WHERE villageid = 1;

-- How many items are there that start with the letter 'A'?
SELECT COUNT(*) FROM ITEM WHERE item LIKE 'A%';

-- How many different jobs are there?
SELECT COUNT(DISTINCT job) FROM INHABITANT;

-- What are the items own by the herbalsist?
SELECT item from ITEM, INHABITANT WHERE INHABITANT.personid = ITEM.owner AND INHABITANT.job = 'Herbalist';