-- SQLite
-- Create a table called Movies with a id as primary key, name, year, budget, category, director, and producer

--
CREATE TABLE Movies (
    id INTEGER PRIMARY KEY,
    name TEXT,
    year INTEGER,
    budget INTEGER,
    category TEXT,
    director TEXT,
    producer TEXT
);

-- Incert Matrix into the table Movies
INSERT INTO Movies (name, year, budget, category, director, producer) VALUES ('Matrix', 1999, 63000000, 'Action', 'Lana Wachowski', 'Joel Silver');

-- Incert Martian into the table Movies
INSERT INTO Movies (name, year, budget, category, director, producer) VALUES ('Martian', 2015, 108000000, 'Sci-Fi', 'Ridley Scott', 'Simon Kinberg');


-- Reading the table Movies
SELECT * FROM Movies;