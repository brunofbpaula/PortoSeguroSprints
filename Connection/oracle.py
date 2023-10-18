import cx_Oracle
import json


# Pegando as credenciais
with open('../credentials.txt', "r") as arquivo:
    credentials = json.load(arquivo)
login = credentials["Login"]
senha = credentials["Password"]

# Conectando ao banco de dados ORACLE
dsn = cx_Oracle.makedsn(host="oracle.fiap.com.br", port=1521, sid="ORCL")
connection = cx_Oracle.connect(user=login, password=senha, dsn=dsn)


