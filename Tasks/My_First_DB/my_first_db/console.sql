CREATE TABLE driver(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO driver (name, email, age) VALUES ('John', 'john@gmail.com', 25);

SELECT name, email FROM driver;
DELETE FROM driver WHERE id = 1;

SELECT * FROM driver;
SELECT COUNT(*) FROM driver;
