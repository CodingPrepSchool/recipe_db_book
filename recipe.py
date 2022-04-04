from flask import Flask, redirect, render_template, request
from recipe_forms import RecipieAdd
import sqlite3
import json


app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route("/", methods = ["GET", "POST"])
def homepage():
    all_recipie = RecipieAdd(csrf_enabled=False)
    con = sqlite3.connect("recipes.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT recipe_id, recipe_name FROM recipes")
    rows = cur.fetchall()
    con.commit()
    con.close
    return render_template("index.html", all_recipie=all_recipie, template_form = all_recipie, rows = rows)

@app.route("/add_recipie", methods=["GET", "POST"])
def addrecipe():
    add_recipie = RecipieAdd(csrf_enabled = False)
    if request.method == 'POST':
        con = sqlite3.connect("recipes.db")
        recipe_name = request.form['recipe_name']
        ingredients= request.form['ingredients'].split(",")
        ingredients_json = json.dumps(ingredients)
        instructions = request.form['instructions'].split(",")
        instructions_json = json.dumps(instructions)
        con.execute("INSERT INTO recipes (recipe_name, ingredients, instructions) VALUES (?, ?, ?)", (recipe_name, ingredients_json, instructions_json))
        con.commit()
        con.close
    return render_template("message.html", add_recipie = add_recipie)

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipes(id):
    all_recipie = RecipieAdd(csrf_enabled=False)
    con = sqlite3.connect("recipes.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT recipe_name, ingredients, instructions FROM recipes WHERE recipe_id=?", [id])
    for row in cur:
        recipe_name = row[0]
        ingredients = json.loads(row[1]) 
        instructions = json.loads(row[2])
    con.commit()
    con.close
    return render_template("recipes_temp.html", all_recipie = all_recipie, recipe_name = recipe_name, ingreidents = ingredients, instructions = instructions)

