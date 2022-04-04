import sqlite3
import json

try:
    sqliteConnection = sqlite3.connect('recipes.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    recipe_name = "Mushroom Omelet"
    ingredients_array = ['Trim off the ends of the mushrooms and cut into thick slices.', 'Heat a large, heavy frying pan over medium-high heat, and add 1 tablespoon of olive oil.', 'Add the shallot, and cook, stirring, until it begins to soften, two or three minutes.', 'Add the mushrooms, and cook, stirring or tossing in the pan, for a few minutes, until they begin to soften and sweat.']

    count = cursor.execute("INSERT INTO recipes (recipe_name, ingredients) VALUES (?, ?)", (recipe_name, json.dumps(ingredients_array)))
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")