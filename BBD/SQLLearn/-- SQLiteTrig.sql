-- SQLite

CREATE TRIGGER increment_usage_count_on_ingredients_linked
AFTER INSERT ON ingredients_recipes
BEGIN
    UPDATE ingredients
    SET usage_count = usage_count + 1
    WHERE id = NEW.ingredient_id;
END;

CREATE TRIGGER decrement_usage_count_on_ingredients_unlinked
AFTER DELETE ON ingredients_recipes
BEGIN
    UPDATE ingredients
    SET usage_count = usage_count - 1
    WHERE id = OLD.ingredient_id;
END;