# Quizz 45
## Part 1 - UML Diagrams of my database
![diagram](Project/Project/g3/assets/documentation/UML.png)

## Part 2 - SQL Queries
```sql
SELECT
  CASE
    WHEN total_deposit - total_withdraw != balance THEN 'bad'
    ELSE 'good'
  END AS 'Status',
  total_deposit,
  total_withdraw,
  balance,
  account_id
FROM (
  SELECT
    SUM(amount) AS total_deposit,
    account_id AS a_d
  FROM transactions
  WHERE transaction_type = 'deposit'
  GROUP BY account_id
),
(
  SELECT
    SUM(amount) AS total_withdraw,
    account_id AS a_w
  FROM transactions
  WHERE transaction_type = 'withdraw'
  GROUP BY account_id
),
accounts
WHERE a_d = a_w
  AND a_d = accounts.account_id;
```
<i>Thanks to Bernardino for crafting this perfect querry</i>

### Proof
![proof](Images/quizz45-proof.png)