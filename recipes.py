from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
import json
from forms import RecipeForm
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route('/')
def index():
    recipe_form = RecipeForm(csrf_enabled=False)
    con = sqlite3.connect("recipes.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT id, recipe_name FROM recipes")
    rows = cur.fetchall()
    con.commit()
    con.close
    return render_template("index.html", rows=rows, template_form=recipe_form)

@app.route('/recipe/<int:id>')
def all_recipies(id):
    recipe_form = RecipeForm(csrf_enabled=False)
    con = sqlite3.connect("recipes.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT recipe_name, ingredients, instructions FROM recipes WHERE id=?", [id])
    for row in cur:
        name = row[0]
        ingredients = json.loads(row[1]) # 
        instructions = json.loads(row[2]) #loads() method can be used to convert a valid JSON string into a Python Dictionary
    con.commit()
    con.close
    return render_template("recipe.html", name=name, instructions = instructions, ingredients = ingredients, template_form=recipe_form)

@app.route("/recipes/add-new", methods=["GET", "POST"])
def new_rec():
    recipe_form = RecipeForm(csrf_enabled=False)
    print(recipe_form)
    if request.method=="POST":
        con = sqlite3.connect("recipes.db")
        cur = con.cursor()
        name = request.form["recipe_name"]
        ingredients = request.form['ingredients'].split(",")
        ingredients_json=json.dumps(ingredients) # dumps() method converts a python object into an equivalent JSON object.
        instructions = request.form["instructions"].split(",")
        instructions_json = json.dumps(instructions)
        cur.execute("INSERT INTO recipes (recipe_name, ingredients, instructions) VALUES (?, ?, ?)", (name, ingredients_json, instructions_json))
        con.commit()
        con.close
    return render_template("message.html")


# The json. load() is used to read the JSON document from file and The json. loads() is used to convert the JSON String document into the Python dictionary.
# dump() method (without “s” in “dump”) used to write Python serialized object as JSON formatted data into a file. The json. dumps() method encodes any Python object into JSON formatted String.

if __name__ == "__main__":
    app.run(debug=True)