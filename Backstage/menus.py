from Backstage import functions
from Backstage import classes
from Connection import scripts
from pandas import to_datetime
from Connection.oracle import connection, cursor
from Connection import oracle


def mensagem_boas_vindas():
    """
    Função que printa uma mensagem de boas-vindas.
    :return: None
    """
    print("[PORTO SEGURO AUTO]")
    print("Bem-vindo (a) ao serviço de seguro auto para veículos pesados da Porto Seguro!")
    functions.new_line()


def menu_login():
    """
    Função que imprime as opções de login, e retorna a escolha do usuário.
    :return: Item escolhido - String.
    """
    print("[ÁREA DE LOGIN]")
    print("Faça login ou inscreva-se agora!")
    print("[C] Cadastro")
    print("[L] Login")
    print("[S] Sair")
    escolha = input("Escolha uma opção: ").upper().strip()
    try:
        while escolha != str(escolha) or escolha != "L" and escolha != "C" and escolha != "S":
            print("[ESCOLHA INVÁLIDA]")
            escolha = input("Escolha uma opção válida: ").upper().strip()
    except MemoryError:
        print("Limite de memória excedido.")
        raise MemoryError
    finally:
        return escolha


def area_login():
    while True:
        escolha = menu_login()

        # Sair
        if escolha == "S":
            return None

        # Cadastro
        elif escolha == "C":
            functions.new_line()
            usuario = cadastro()
            if usuario:
                return usuario
            functions.new_line()
            continue

        # Login
        elif escolha == "L":
            functions.new_line()
            usuario = logar()
            functions.new_line()
            if usuario:
                return usuario
            else:
                continue
        else:
            print("Oops!")  # Nunca vai executar... eu acho.
            return


def cadastro():
    print("[NOVO CADASTRO]")
    print("Crie seu login preenchendo as informações abaixo.")
    functions.delay(0.4)
    functions.new_line()
    refazer = "R"
    while refazer == "R":
        nome = functions.nome_cliente()
        dt_nascimento = functions.dt_nascimento_cliente()
        nr_cpf = functions.nr_cpf_cliente()
        email = functions.email_cliente()
        senha = functions.senha_cliente()
        genero = input('[GÊNERO] Como você se identifica.\nDigite o seu gênero: ')
        usuario = classes.Cliente(nome, dt_nascimento, nr_cpf, email, senha)
        functions.delay(0.4)
        functions.new_line()
        print("[CONFIRMAÇÃO]")
        print("Certifique-se de que todos os dados fornecidos estão corretos.")
        print("[C] Continuar")
        print("[R] Refazer")
        refazer = input("Escolha uma opção: ").upper().strip()
        while refazer != str(refazer) or refazer != "C" and refazer != "R":
            print("[ESCOLHA UMA OPÇÃO VÁLIDA]")
            refazer = input("Escolha uma opção: ").upper().strip()
        if refazer == "C":
            functions.new_line()
            functions.delay(1)

            # Salva na tabela de clientes
            dados_cliente = [usuario.nr_cpf,
                             usuario.nome,
                             usuario.idade,
                             to_datetime(usuario.dt_nascimento),
                             genero]
            scripts.scripts_cliente('INSERT', dados_cliente)

            # Salva na tabela de login
            dados_login = [usuario.email,
                           usuario.senha,
                           'A']
            scripts.scripts_login('INSERT', lista=dados_login, cpf=usuario.nr_cpf)

            print("[TUDO CERTO]")
            print("Salvando...")
            functions.delay(1)
            functions.new_line()

            return usuario

        elif refazer == "R":
            print("Tudo bem! Tente novamente.")
            functions.new_line()
            continue


def logar():
    """
    Função que loga o usuário, validando CPF e senha.
    :return: Objeto do cliente.
    """
    while True:
        print("[LOGIN]\n"
              "Acesse o menu com seu login.")

        # Valida login
        nr_cpf = input("[NÚMERO DE CPF] Digite o seu CPF: ")
        if '.' in nr_cpf or '-' in nr_cpf:
            nr_cpf = ''.join(filter(str.isdigit, nr_cpf))
        senha = input("[SENHA] Digite a sua senha: ")
        try:
            usuario = scripts.scripts_login('VALIDAR', cpf=nr_cpf, senha=senha)
        # CPF não existe
        except KeyError:
            print("\n[CPF NÃO ENCONTRADO]")
            escolha = functions.tentar_novamente()
            if escolha == "S":
                functions.new_line()
                continue
            else:
                break

        # Senha incorreta
        except ValueError:
            print("\n[SENHA INCORRETA]")
            escolha = functions.tentar_novamente()
            functions.new_line()
            if escolha == "S":
                continue
            else:
                break

        # Login não é cadastrado
        except AssertionError:
            print("\n[LOGIN NÃO LOCALIZADO]")
            escolha = functions.tentar_novamente()
            functions.new_line()
            if escolha == "S":
                continue
            else:
                break

        if usuario:
            print('Entrando...')
            functions.delay(2)
            return usuario


def itens_menu(nome):
    """
    Função que printa os itens do menu principal.
    :param nome: Nome do usuário.
    :return: None
    """
    print("[MENU PRINCIPAL]")
    print(f"{nome}, por favor, selecione um dos itens abaixo: ")
    print("[1] MEUS VEÍCULOS")
    print("[2] AVISO DE SINISTRO")
    print("[3] VOLTAR PARA LOGIN")
    print("[4] SAIR")


def menu(usuario):
    """
    Função que imprime e controla o fluxo do menu, contém todos os itens.
    :param usuario: Objeto cliente, com dados do usuário.
    :return: None.
    """
    while True:

        # Se o objeto não existe, o usuário escolheu sair
        if not usuario:
            functions.new_line()
            return

        # Nome do usuário
        nome = usuario.nome.split(" ")[0]

        # Escolhendo item do menu
        itens_menu(nome)
        escolha = functions.escolher_item()
        functions.new_line()

        # Meus veículos
        if escolha == 1:
            meus_veiculos(usuario)
            continue

        # Aviso de sinistro
        elif escolha == 2:
            aviso_sinistro(usuario)
            functions.new_line()
            functions.delay(3)
            continue

        # Voltar para o login
        elif escolha == 3:
            usuario = area_login()
            continue

        # Sair do menu
        else:

            # Fecha conexão
            cursor.close()
            connection.close()

            break
    return


# Meus veículos
def meus_veiculos(usuario):
    print('[MEUS VEÍCULOS]\n'
          'Escolha uma ação.\n'
          '[A] Adicionar veículo\n'
          '[D] Deletar veículo\n'
          '[E] Editar veículo\n'
          '[V] Visualizar veículos\n'
          '[M] Voltar ao menu')

    # Força escolha
    opcoes = ['A', 'D', 'E', 'V']
    while True:
        escolha = input("Digite a ação desejada: ")
        if escolha.upper() in opcoes:
            functions.new_line()
            break
        else:
            print("[AÇÃO INVÁLIDA]")

    # CRUD
    escolha.upper()
    # Insert
    if escolha == "A":
        print('[NOVO VEÍCULO]')
        dados = dados_veiculo('INSERT')
        scripts.scripts_veiculo('INSERT', cpf=usuario.nr_cpf, lista=dados)
        print('[ADICIONADO] Tudo certo.\n'
              'Voltando...')
        functions.new_line()
        functions.delay(3)

    # Delete
    elif escolha == 'D':
        functions.delay(1)
        print('[ATENÇÃO]')
        print('Essa ação não pode ser desfeita. Continuar?')
        opcao = functions.confirmar()
        if opcao == 1:
            chassi = input('Digite o número do chassi do veículo a ser deletado: ')
            scripts.scripts_veiculo('DELETE', chassi=chassi)
            print('[DELETADO] Removido com sucesso.\n'
                  'Voltando...')
            functions.new_line()
            functions.delay(3)
        else:
            print('Voltando...')
            functions.delay(1.5)

    # Update
    elif escolha == 'E':
        print('[ATUALIZAR VEÍCULO]\n'
              'Informe os dados a seguir para atualizar um veículo.')
        dados = dados_veiculo('UPDATE')
        scripts.scripts_veiculo('UPDATE', lista=dados)
        print('[ATUALIZADO] Tudo certo.\n'
              'Voltando...')
        functions.new_line()
        functions.delay(3)

    # Select
    elif escolha == 'V':

        # Pega ID
        id_cliente = oracle.select('SELECT id_cliente FROM T_POR_CLIENTE WHERE nr_cpf = ', usuario.nr_cpf)
        comando = 'SELECT nm_chassi, marca, modelo, nm_ano, nm_placa, ' \
                  'blindagem, tp_combustivel FROM T_POR_VEICULO WHERE id_cliente = '

        # Executa query
        query = comando + str(id_cliente[0])
        cursor.execute(query)
        result = cursor.fetchall()
        veiculos = result
        for veiculo in veiculos:

            # Formata blindagem
            blindagem = veiculo[-2]
            if blindagem == 0:
                blindagem = 'NÃO'
            else:
                blindagem = 'SIM'

            # Imprime veículos
            print(f'[VEÍCULO] {veiculo[1]} {veiculo[2]} {veiculo[3]}\n'
                  f'[NÚMERO DE CHASSI] {veiculo[0]}\n'
                  f'[VEÍCULO BLINDADO] {blindagem}\n'
                  f'[TIPO DE COMBUSTÍVEL] {veiculo[-1]}\n')
            functions.delay(2.5)
        print('Voltando...\n')
        functions.delay(1)

    elif escolha == 'M':
        print('Voltando...')
        functions.delay(2)
        return


def dados_veiculo(comando):

    dados = []

    refazer = "R"
    while refazer == "R":
        if comando == 'UPDATE':
            nm_chassi = input('[NÚMERO DE CHASSI] Digite o número de chassi do veículo a ser modificado: ')
            print('[NOVOS DADOS] Digite os novos dados do veículo!')
        else:
            nm_chassi = input('[NÚMERO DE CHASSI] Digite o número de chassi: ')
        marca = input('[MARCA] Digite a marca do veículo: ')
        modelo = input('[MODELO] Digite o modelo do veículo: ')

        nm_ano = int(input('[ANO DE FABRICAÇÃO] Digite o ano de fabricação do veículo: '))
        while nm_ano != int(nm_ano):
            print('[DIGITE UM ANO VÁLIDO]')
            nm_ano = int('Digite o ano de fabricação do veículo: ')

        placa = input('[PLACA] Digite o número da placa do veículo: ')

        blindagem = input('[BLINDAGEM] O veículo possui blindagem?: ')
        while blindagem.upper() not in ['SIM', 'NÃO', 'S', 'N']:
            print('[RESPOSTA INESPERADA]')
            blindagem = input('\n[BLINDAGEM] O veículo possui blindagem?: ')
        if blindagem == 'SIM' or blindagem == 'S':
            blindagem = 1
        else:
            blindagem = 0

        combustivel = input('[COMBUSTÍVEL] Digite o tipo de combustível utilizado: ')

        functions.delay(0.4)
        functions.new_line()

        # Confirmação
        print("[CONFIRMAÇÃO]")
        print("Certifique-se de que todos os dados fornecidos estão corretos.")
        print("[C] Continuar")
        print("[R] Refazer")
        refazer = input("Escolha uma opção: ").upper().strip()
        while refazer != str(refazer) or refazer != "C" and refazer != "R":
            print("[ESCOLHA UMA OPÇÃO VÁLIDA]")
            refazer = input("Escolha uma opção: ").upper().strip()

        if refazer == "C":
            functions.new_line()
            functions.delay(1)

            if comando == 'INSERT':
                dados = [nm_chassi, marca, modelo, nm_ano, placa, blindagem, combustivel]
            elif comando == 'UPDATE':
                dados = [marca, modelo, nm_ano, placa, blindagem, combustivel, nm_chassi]
            return dados

        elif refazer == "R":
            print("Tudo bem! Tente novamente.")
            functions.new_line()
            continue


def aviso_sinistro(usuario):
    # Opções
    print('[AVISO DE SINISTRO]\n'
          'Escolha uma ação.\n'
          '[S] Solicitar socorro\n' 
          '[D] Deletar socorro\n'
          '[P] Meus pedidos de socorro\n'
          '[M] Voltar ao menu')

    # Força escolha
    opcoes = ['S', 'D', 'P', 'M']
    while True:
        escolha = input("Digite a ação desejada: ")
        if escolha.upper() in opcoes:
            functions.new_line()
            break
        else:
            print("[AÇÃO INVÁLIDA]")

    # CRUD
    escolha = escolha.upper()
    # INSERT
    if escolha == 'S':
        print('[SOLICITAÇÃO DE SOCORRO]\n'
              'Informe os dados a seguir para conseguir assistência.')

        refazer = "R"
        while refazer == "R":

            nm_chassi = input('[VEÍCULO DANIFICADO] Informe o número de chassi do veículo: ')
            sinistro = dados_sinistro()
            local = dados_local()

            functions.delay(0.4)
            functions.new_line()

            # Confirmação
            print("[CONFIRMAÇÃO]")
            print("Certifique-se de que todos os dados fornecidos estão corretos.")
            print("[C] Continuar")
            print("[R] Refazer")
            refazer = input("Escolha uma opção: ").upper().strip()
            while refazer != str(refazer) or refazer != "C" and refazer != "R":
                print("[ESCOLHA UMA OPÇÃO VÁLIDA]")
                refazer = input("Escolha uma opção: ").upper().strip()

            if refazer == "C":
                functions.new_line()
                functions.delay(1)

                scripts.scripts_ocorrencia(comando='INSERT', sinistro=sinistro, local=local, nr_cpf=usuario.nr_cpf,
                                           chassi=nm_chassi)
                print('[ADICIONADO] Tudo certo.\n'
                      'V'
                      'Voltando...')
                functions.new_line()
                functions.delay(3)

            elif refazer == "R":
                print("Tudo bem! Tente novamente.")
                functions.new_line()
                continue

    # SELECT
    elif escolha == 'P':

        pedidos = scripts.scripts_ocorrencia('SELECT', nr_cpf=usuario.nr_cpf)
        if pedidos:
            for pedido in pedidos:

                # Imprime veículos
                print(f'[IDENTIFICADOR SINISTRO] {pedido[0]}\n'
                      f'[SOLICITANTE] {pedido[1]}\n'
                      f'[VEÍCULO] {pedido[2]} {pedido[3]} {pedido[4]}\n'
                      f'[PLACA DO VEÍCULO] {pedido[5]}\n'
                      f'[SINISTRO] {pedido[6]} - {pedido[7]}\n'
                      f'[LOCAL DO SINISTRO] {pedido[-2]} {pedido[-1]}\n')
                functions.delay(2.5)
            print('Voltando...')
            functions.delay(1)
        else:
            print('[NENHUM PEDIDO ENCONTRADO]')
            print('Voltando...')
            functions.delay(1)

    # DELETE
    elif escolha == 'D':
        functions.delay(1)
        print('[ATENÇÃO]')
        print('Essa ação não pode ser desfeita. Continuar?')
        opcao = functions.confirmar()
        if opcao == 1:
            ident = input('Digite o identificador do aviso de sinistro a ser deletado: ')
            scripts.scripts_ocorrencia('DELETE', identificador=ident)
            print('\n[DELETADO] Removido com sucesso.\n'
                  'Voltando...')
            functions.delay(3)
        else:
            print('Voltando...')
            functions.delay(1.5)

    # MENU
    elif escolha == 'M':
        print('Voltando...')
        functions.delay(1)


def dados_local():

    rua = input('[NOME DA RUA] Digite a rua: ')
    nr = input('[NÚMERO DA RUA] Digite o número da rua: ')
    sentido = input('[SENTIDO DA VIA] Crescente ou decrescente: ')
    while sentido.upper() not in ['CRESCENTE', 'C', 'CRESC', 'D', 'DESC', 'DECRESCENTE']:
        print('[RESPOSTA INESPERADA]')
        sentido = input('[SENTIDO DA VIA] Crescente ou decrescente: ')

    if sentido.upper() in ['CRESCENTE', 'C', 'CRESC']:
        sentido = 'C'
    else:
        sentido = 'D'

    dados = [nr, rua, sentido]
    return dados


def dados_sinistro():

    sinistro = input('[SINISTRO] Digite o problema: ')
    causa = input('[CAUSA] O que causou o problema: ')
    descricao = input('[DESCRIÇÃO] Descreva um breve resumo do ocorrido: ')

    dados = [sinistro, causa, descricao]
    return dados


if __name__ == "__main__":

    print('Antiga implementação')
    # mensagem_boas_vindas()
    # dic = {}
    # dic, cpf = area_login(dic)
    # menu(dic, cpf)
    # functions.volte_sempre()
