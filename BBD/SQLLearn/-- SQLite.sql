-- SQLite
CREATE TABLE posts (
    title VARCHAR(150),
    content TEXT,
    category VARCHAR(60),
    createdAT DATETIME
);
ALTER TABLE posts DROP createdAt;
ALTER TABLE posts ADD createdAt DATETIME;
ALTER TABLE posts RENAME category TO tag;
DROP TABLE posts
