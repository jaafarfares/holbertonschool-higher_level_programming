-- create a dataabase and a table
CREATE dataabase IF NOT EXISTS hbtn_0d_us;
CREATE TABLE if NOT EXISTS states
(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256)
);
