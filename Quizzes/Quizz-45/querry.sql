-- SQLite

SELECT name FROM sqlite_master WHERE type='table';

SELECT * FROM sqlite_sequence;

SELECT * FROM customers;

SELECT * FROM accounts;

SELECT * FROM transactions;

-- add all the deposits in the transactions table and subtract all the withdrawals and current balance with case statement and add a collumn for current balance
SELECT account_id, SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE 0 END) - SUM(CASE WHEN transaction_type = 'withdrawal' THEN amount ELSE 0 END) AS current_balance FROM transactions GROUP BY account_id;
