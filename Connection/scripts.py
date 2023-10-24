from Connection import oracle
from pandas import to_datetime
from Backstage.functions import delay


def scripts_cliente(comando, lista=None, id=None, variavel=None):
    """
    Função que executa um comando de data modeling na tabela T_POR_CLIENTE.
    :param variavel: Variável a ser atualizada no comando UPDATE.
    :param comando: Comando de data modeling.
    :param lista: Lista de valores do cliente.
    :param id: Identificação do cliente.
    :return: None ou lista de valores do SELECT.
    """

    if comando == 'INSERT':
        oracle.insert('INSERT INTO T_POR_CLIENTE(id_cliente, nr_cpf, nome_completo, idade, dt_nascimento, genero)'
                      'VALUES (:id_cliente, :nr_cpf, :nome_completo, :idade, :dt_nascimento, :genero)', lista)

    elif comando == 'DELETE':
        oracle.delete('DELETE FROM T_POR_CLIENTE WHERE id_cliente = :id_cliente', id)

    elif comando == 'UPDATE':
        oracle.update(f'UPDATE T_POR_CLIENTE SET {variavel} = :v WHERE id_cliente = :id_cliente', lista)

    elif comando == 'SELECT':
        values = oracle.select('SELECT * FROM T_POR_CLIENTE WHERE id_cliente = ', id)
        return values

    else:
        print('ERROR')

    return


if __name__ == "__main__":

    # Testando INSERT e DELETE
    data_nascimento = to_datetime('2004-08-04')
    lipe = [9, 11732549742, 'Felipe de Almeida Cardoso', 19, data_nascimento, 'Homem']
    scripts_cliente('INSERT', lista=lipe)
    delay(5)
    scripts_cliente('DELETE', id=9)

    # Testando UPDATE
    data_nascimento = to_datetime('2005-05-09')
    miguel = [8, 97842239643, 'Miguel Ribeiro de Noce', 18, data_nascimento, 'Mulher Trans']
    scripts_cliente('INSERT', lista=miguel)
    # Valores do comando
    delay(5)
    atualizar = ['Homem', miguel[0]]
    scripts_cliente('UPDATE', lista=atualizar, variavel='genero')
