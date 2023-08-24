from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NewProductForm(FlaskForm):
    name = StringField("Ingrese Producto:")
    precio = StringField("Ingrese Precio:")
    submit = SubmitField("Registrar")