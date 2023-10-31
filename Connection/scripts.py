from Connection import oracle
from pandas import to_datetime
from Backstage.functions import delay


def scripts_cliente(comando, lista=None, nr_cpf=None, variavel=None):
    """
    Função que executa um comando de data modeling na tabela T_POR_CLIENTE.
    :param variavel: Variável a ser atualizada no comando UPDATE.
    :param comando: Comando de data modeling.
    :param lista: Lista de valores do cliente.
    :param nr_cpf: CPF do cliente.
    :return: None ou lista de valores do SELECT.
    """
    comando.upper()

    if comando == 'INSERT':
        oracle.insert('INSERT INTO T_POR_CLIENTE(id_cliente, nr_cpf, nome_completo, idade, dt_nascimento, genero)'
                      'VALUES (T_POR_CLIENTE_seq.nextval, :nr_cpf, :nome_completo, '
                      ':idade, :dt_nascimento, :genero)', lista)

    elif comando == 'DELETE':
        oracle.delete('DELETE FROM T_POR_CLIENTE WHERE nr_cpf = :nr_cpf', nr_cpf)

    elif comando == 'UPDATE':
        oracle.update(f'UPDATE T_POR_CLIENTE SET {variavel} = :v WHERE nr_cpf = :nr_cpf', lista)

    elif comando == 'SELECT':
        values = oracle.select('SELECT * FROM T_POR_CLIENTE WHERE id_cliente = ', nr_cpf)
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
    scripts_cliente('DELETE', nr_cpf=11732549742)

    # Testando UPDATE
    data_nascimento = to_datetime('2005-05-09')
    miguel = [8, 97842239643, 'Miguel Ribeiro de Noce', 18, data_nascimento, 'Mulher Trans']
    scripts_cliente('INSERT', lista=miguel)
    # Valores do comando
    delay(5)
    atualizar = ['Homem', miguel[0]]
    scripts_cliente('UPDATE', lista=atualizar, variavel='genero')

    # Testando sequence
    data_nascimento = to_datetime('1992-10-22')
    savage = [87342579091, 'Shéyaa Bin Abraham-Joseph', 31, data_nascimento, 'Homem']
    scripts_cliente('INSERT', lista=savage)
    scripts_cliente('DELETE', nr_cpf=savage[0])
