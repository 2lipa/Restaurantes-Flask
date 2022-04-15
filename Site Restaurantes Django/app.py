from flask import Flask, render_template
from lista_restaurante import restaurante_lista

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("principal.html", loja=restaurante_lista)

@app.route('/Restaurante/<id>')
def loja(id):
    return render_template("loja.html", loja=restaurante_lista[int(id)])