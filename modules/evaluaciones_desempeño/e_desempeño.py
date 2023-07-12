from flask import Blueprint, render_template, redirect, session, request

e_desempeño = Blueprint('e_desempeño', __name__, template_folder="templates_e_desempeño", static_folder="statics_e_desempeño")

@e_desempeño.route('/e_desempeño')
def index_e_desempeño():
    return render_template('index_e_desempeño.html')




