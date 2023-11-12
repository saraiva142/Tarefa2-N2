import sqlite3
from flask import g
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resultado", methods=['POST'])
def resultado():
    con = sqlite3.connect('database.db')
    nome = request.form["nome"]
    n1 = float(request.form["nota1"])
    n2 = float(request.form["nota2"])
    media = (n1 + n2) / 2
    cur = con.cursor()
    cur.execute("INSERT INTO alunos (nome,n1,n2,media) VALUES (?,?,?,?)", (nome,n1,n2,media))
    con.commit()
    con.close()
    return render_template("resultado.html", nome=nome, media=media)

@app.route("/alunos")
def listar():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM alunos")
    rows = cur.fetchall()
    con.close()
    return render_template("listar.html", rows = rows)


app.run(debug=True)
