from flask import Blueprint, render_template, redirect, request

encuestas = Blueprint('Encuestas', __name__, template_folder="encuestas_templates", static_folder="statics_templates")

@encuestas.route('/encuestas')
def index_encustas():
    return render_template('encuestas.html')



