import pyodbc
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
    # Parâmetros de conexão
    dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-UTVRFMC\SQL;"
    "Database=TarefaTres;"
    )

    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    id = int(request.form["id"])
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    telefone = int(request.form["telefone"])
    email = request.form["email"]
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO CONTATOS(ID, NOME, SOBRENOME, TELEFONE, EMAIL) VALUES (?, ? , ? , ? , ? )", (id,nome,sobrenome,telefone,email))
    conexao.commit()
    cursor.execute("SELECT * FROM CONTATOS WHERE [NOME] = (?) AND [SOBRENOME] = (?) AND [TELEFONE] = (?) AND [EMAIL] = (?)", (nome, sobrenome, telefone, email))
    rows = cursor.fetchall()
    conexao.close()
    return render_template("resultado.html", rows = rows)

@app.route("/alunos")
def listar():
    # Parâmetros de conexão
    dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-UTVRFMC\SQL;"
    "Database=TarefaTres;"
    )

    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM CONTATOS")
    rows = cursor.fetchall()
    conexao.close()
    return render_template("listar.html", rows = rows)


app.run(debug=True)
