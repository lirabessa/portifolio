from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/projetos')
def projetos():
    return render_template("projetos.html")

@app.route('/contato')
def contato():
    return render_template("contato.html")