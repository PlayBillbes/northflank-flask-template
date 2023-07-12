from flask import Blueprint, render_template, request, redirect

r_personal = Blueprint('Control_Rotación_Personal', __name__, template_folder="tempaltes_r_personal", static_folder="statics_r_personal")

@r_personal.route('/control_rotacion_personal')
def index_r_personal():
    return render_template('control_rotacion_personal.html')

# Requisicion de personal
# Ingreso de Personal
# Retiro de Personal
# control paz y salvos
# Control re integros


