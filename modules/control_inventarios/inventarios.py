from flask import Blueprint, render_template, redirect, request

inventarios = Blueprint('Inventarios', __name__, template_folder="templates_inventarios", static_folder="statics_inventarios")

@inventarios.route('/inventarios')
def index_inventarios():
    return render_template('inventarios.html')





