-- create a dataabase and a table
CREATE dataabase IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE if NOT EXISTS states
(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
