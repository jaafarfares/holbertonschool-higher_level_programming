-- script that creates the table with id not null
CREATE TABLE IF NOT EXISTS unique_id
(
    id  INT NEWID(1),
    name VARCHAR(256)
);
