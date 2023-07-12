from flask import Blueprint, render_template, redirect, request, session

index = Blueprint('Index', __name__, template_folder="templates_index", static_folder="statics_index")

@index.route('/')
def home():
    return render_template('home.html')

@index.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@index.route('/nuestros_servicios')
def nuestros_servicios():
    return render_template('nuestros_servicios.html')

@index.route('/casos_de_exito')
def casos_de_exito():
    return render_template('casos_de_exito.html')

@index.route('/provar_nuestros_servicios')
def provar_nuestros_servicios():
    return render_template('provar_nuestros_servicios.html')

