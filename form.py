from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired


class NewRecipe(FlaskForm):
    name = StringField("Name of the Recipe", validators = [DataRequired()])
    ingredients = TextAreaField("Ingredients", validators = [DataRequired()])
    instructions = TextAreaField("Instructions", validators = [DataRequired()])
    submit = SubmitField("Submit")