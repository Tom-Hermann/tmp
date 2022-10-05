-- SQLite
SELECT COUNT(id), duration
FROM recipes
GROUP BY duration;

SELECT DISTINCT r.id, r.title, r.slug
FROM recipes
JOIN categories_recipes cr ON cr.recipe_id = r.id
JOIN categories c ON c.id = cr.category_id
WHERE c.title = 'Dessert';

SELECT *
FROM recipes r
WHERE r.created_at DESC

SELECT *
FROM recipes r
LIMIT 10 OFFSET 20