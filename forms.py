from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, TextAreaField, SubmitField, validators, StringField
from wtforms.validators import DataRequired


class RecipeForm(FlaskForm):
    recipe_name=StringField("Recipe Name", validators = [DataRequired()])
    ingredients = TextAreaField("Ingredients", validators = [DataRequired()])
    instructions = TextAreaField("Instructions", validators = [DataRequired()])
    submit = SubmitField("Add Recipe")