import pyodbc


# Parâmetros de conexão
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-UTVRFMC\SQL;"
    "Database=TarefaTres;"
)

conexao = pyodbc.connect(dados_conexao)
print('DEU CERTO')

cursor = conexao.cursor()

comando = """
INSERT INTO CONTATOS(ID, NOME, SOBRENOME, TELEFONE, EMAIL) VALUES (2, 'testePY', 'testesPY', 19191929, 'aahags@gmail.com')

"""

cursor.execute(comando)
cursor.commit()