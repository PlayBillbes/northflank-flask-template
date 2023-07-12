from flask import Blueprint, render_template, redirect, request

rendimiento = Blueprint('Rendimiento', __name__, template_folder="templates_rendimiento", static_folder="statics_rendimiento")

@rendimiento.route('/rendimiento')
def index_rendimiento():
    return render_template('rendimiento.html')




