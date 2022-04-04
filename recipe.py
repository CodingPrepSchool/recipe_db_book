from flask import Flask,render_template,request
import sqlite3
import json
from form import NewRecipe

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


@app.route("/")
def index_page():
    new_recipe = NewRecipe(csrf_enabled=False)
    con = sqlite3.connect("recipe.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT recipe_id,recipe_name FROM recipe")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return render_template("index.html",rows = rows, template_form = new_recipe)

@app.route("/recipe/add", methods=["GET","POST"])
def new_recipe():
    if request.method == "POST":
        con = sqlite3.connect("recipe.db")
        cur = con.cursor()
        name = request.form["name"]
        ingredients = request.form["ingredients"].split(",")
        ingredients_json = json.dumps(ingredients)
        instructions = request.form["instructions"].split(",")
        instructions_json = json.dumps(instructions)
        cur.execute("INSERT INTO recipe (recipe_name,ingredients,instructions) values(?,?,?)",(name,ingredients_json,instructions_json))
        con.commit()
        con.close()
        return render_template("message.html")


if __name__ == "__main__":
    app.run(debug=True)