# Quizz 43

## Query:

```sql
-- SQLite
CREATE TABLE Movies (
    id INTEGER PRIMARY KEY,
    name TEXT,
    year INTEGER,
    budget INTEGER,
    category TEXT,
    director TEXT,
    producer TEXT
);

-- Incerting Matrix into the table Movies
INSERT INTO Movies (name, year, budget, category, director, producer) VALUES ('Matrix', 1999, 63000000, 'Action', 'Lana Wachowski', 'Joel Silver');

-- Incerting Martian into the table Movies
INSERT INTO Movies (name, year, budget, category, director, producer) VALUES ('Martian', 2015, 108000000, 'Sci-Fi', 'Ridley Scott', 'Simon Kinberg');


-- Readinging the table Movies
SELECT * FROM Movies;

```

![](/Images/quizz43-proof.png)