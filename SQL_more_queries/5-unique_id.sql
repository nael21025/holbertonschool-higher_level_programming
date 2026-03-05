-- Creates table unique_id with UNIQUE and DEFAULT 1 on id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
