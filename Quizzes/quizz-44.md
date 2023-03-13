# Quizz 44
## SQL Queries
List all tables in the database
```sql
SELECT * FROM table_name;
```
Get Friendly and male inhabitants
```sql
SELECT * FROM INHABITANT WHERE gender = "Male" AND state = 'Friendly';
```
What is the average gold of all inhabitants in village 1?
```sql
SELECT AVG(gold) FROM INHABITANT WHERE village_id = 1;
```
How many items are there that start with the letter 'A'?
```sql
SELECT COUNT(*) FROM ITEM WHERE item LIKE 'A%';
```
How many different jobs are there?
```sql
SELECT COUNT(DISTINCT job) FROM INHABITANT;
```
What are the items own by the herbalsist?
```sql
SELECT item from ITEM, INHABITANT WHERE INHABITANT.personid = ITEM.owner AND INHABITANT.job = 'Herbalist';
```

## Proof
![](/Images/quizz44-proof.png)