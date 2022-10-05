-- SQLite
INSERT INTO posts (
    title,
    content,
    tag,
    createdAt
) VALUES (
    '1TOTO',
    '2TITI',
    '3TATA',
    16516566
);

SELECT title, tag
FROM posts;

SELECT *
FROM posts;

SELECT *
FROM posts
WHERE createdAt < 165165660;

SELECT *
FROM posts
WHERE createdAt < 165165660 AND title != '1TOTO';

SELECT *
FROM posts
WHERE createdAt < 165165660 AND title IN ('1TOTO', 'TITI');

SELECT *
FROM posts
WHERE createdAt < 165165660 AND (title != '1TOTO' OR content == '2TITI');


SELECT *
FROM posts
WHERE title LIKE '1%OT%';

UPDATE posts SET title = 'Test' WHERE title LIKE '1%';