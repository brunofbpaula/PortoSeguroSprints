import cx_Oracle
import json
from pandas import to_datetime
# Pegando as credenciais
with open('../credentials.txt', "r") as arquivo:
    credentials = json.load(arquivo)
login = credentials["Login"]
senha = credentials["Password"]

# Conectando ao banco de dados ORACLE
dsn = cx_Oracle.makedsn(host="oracle.fiap.com.br", port=1521, sid="ORCL")
connection = cx_Oracle.connect(user=login, password=senha, dsn=dsn)
cursor = connection.cursor()


# Funções CRUD
def insert(comando, *args):
    """
    Função que realiza comando de INSERT nas tabelas T_POR.
    :type args: Valores a serem inseridos.
    :param comando: Comando SQL.
    :return: Confirmação.
    """
    while True:

        # Valores
        values = list(args)

        try:

            # Query
            cursor.execute(comando, tuple(values))
            connection.commit()
            break

        # Chave já existente
        except cx_Oracle.IntegrityError:
            print("O ID digitado já existe.")
            values[0] = int(input("Digite um novo valor de ID: "))

    return 'Cadastrado.'


if __name__ == "__main__":
    id = 1
    cpf = 121007987
    nome = 'Bruno Blackout'
    idade = 19
    dt_nascimento = to_datetime('2004-09-29')
    genero = 'Homem Cis'

    print(insert('INSERT INTO T_POR_CLIENTE(id_cliente, nr_cpf, nome_completo, idade, dt_nascimento, genero)VALUES '
                 '(:id_cliente, :nr_cpf, :nome_completo, :idade, :dt_nascimento, :genero)',
                 id, cpf, nome, idade, dt_nascimento, genero))

    cursor.close()
    connection.close()
