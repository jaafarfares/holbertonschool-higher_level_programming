-- script that creates the table with a unique id
CREATE TABLE IF NOT EXISTS unique_id
(
    id INT DEFAULT 1 UNIQU,
    name VARCHAR(256)
);
