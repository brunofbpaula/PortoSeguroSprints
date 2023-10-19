import cx_Oracle
import json
from Backstage.functions import delay
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
def insert(comando, lista):
    """
    Função que realiza comando de INSERT nas tabelas T_POR.
    :param lista: Valores a serem inseridos.
    :param comando: Comando SQL.
    :return: None.
    """
    while True:
        try:

            # Query
            cursor.execute(comando, tuple(lista))
            connection.commit()
            break

        # Chave já existente
        except cx_Oracle.IntegrityError:
            print("O ID digitado já existe.")
            values[0] = int(input("Digite um novo valor de ID: "))

    print('\n[CADASTRADO COM SUCESSO]\n')
    return


def delete(comando, id_pk):
    """
    Função para executar um comando de delete.
    :param comando: Comando SQL.
    :param id_pk: Chave primária da tabela.
    :return: None
    """
    value = (id_pk,)
    cursor.execute(comando, value)
    connection.commit()

    print('\n[DELETADO COM SUCESSO]\n')


if __name__ == "__main__":

    # Criando usuário de teste
    id_cliente = 5
    nr_cpf = 41983248721
    nome = 'Billie Eilish Pirate Baird O\'Connell'
    idade = 21
    dt_nascimento = to_datetime('2001-12-18')  # Requer uma conversão para datatime
    genero = 'Mulher'
    values = [id_cliente, nr_cpf, nome, idade, dt_nascimento, genero]

    # Testando insert - OK
    print(f'Adicionando {nome}...')
    insert('INSERT INTO T_POR_CLIENTE(id_cliente, nr_cpf, nome_completo, idade, dt_nascimento, genero)VALUES '
           '(:id_cliente, :nr_cpf, :nome_completo, :idade, :dt_nascimento, :genero)', values)

    # Testando delete - OK
    delay(2)
    print(f'Deletando {nome}...')
    delete('DELETE FROM T_POR_CLIENTE WHERE id_cliente = :id_cliente', id_cliente)

    cursor.close()
    connection.close()
