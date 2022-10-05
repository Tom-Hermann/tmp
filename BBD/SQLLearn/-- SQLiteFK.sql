-- SQLite
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title VARCHAR(150) NOT NULL,
    description TEXT
);

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title VARCHAR(150) NOT NULL,
    slug VARCHAR(150) NOT NULL,
    content TEXT,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
);

INSERT INTO categories (title)
VALUES ('Plat'), ('Dessert');

INSERT INTO recipes (title, slug, category_id)
VALUES
    ('Crême anglaise', 'creme-anglaise', 2),
    ('Soupe', 'soupe', 1),
    ('Salade de fruit', 'salade-de-fruit', 2);

SELECT r.id, r.title, c.title AS category
FROM recipes r
JOIN categories c ON c.id = r.category_id;