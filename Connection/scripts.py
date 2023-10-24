from Connection import oracle


def scripts_cliente(comando, lista=None, id=None):
    """
    Função que executa um comando de data modeling na tabela T_POR_CLIENTE.
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
        oracle.update('UPDATE T_POR_CLIENTE SET idade = :idade WHERE id_cliente = :id_cliente', lista)

    elif comando == 'SELECT':
        values = oracle.select('SELECT * FROM T_POR_CLIENTE WHERE id_cliente = ', id)
        return values

    else:
        print('ERROR')

    return
