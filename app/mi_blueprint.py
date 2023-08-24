from flask import Blueprint

#Creacion y configuracion blueprint

mi_blueprint = Blueprint('mi_blueprint', __name__, url_prefix= '/ejemplo')

#Crear ruta para blueprint

@mi_blueprint.route('/saludo')
def saludo():
    return "<h2> El que tiene hambre en pan piensa (‾◡◝) <h2>"