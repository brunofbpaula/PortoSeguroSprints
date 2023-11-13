from Backstage import functions
from Backstage import classes
from Connection import scripts
from pandas import to_datetime
from Connection.oracle import connection, cursor


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
        print("[ÁREA DE LOGIN]")

        # Valida login
        nr_cpf = input("Digite o seu CPF: ")
        if '.' in nr_cpf or '-' in nr_cpf:
            nr_cpf = ''.join(filter(str.isdigit, nr_cpf))
        senha = input("Digite a sua senha: ")
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
            print("[AVISO DE SINISTRO]")
            print("EM MANUTENÇÃO. TENTE NOVAMENTE MAIS TARDE.")
            functions.new_line()
            functions.delay(3)
            continue

        # Voltar para o login
        elif escolha == 4:
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
          'Escolha uma ação\n'
          '[A] Adicionar veículo\n'
          '[D] Deletar veículo\n'
          '[E] Editar veículo\n'
          '[V] Visualizar veículos')


if __name__ == "__main__":

    print('Antiga implementação')
    # mensagem_boas_vindas()
    # dic = {}
    # dic, cpf = area_login(dic)
    # menu(dic, cpf)
    # functions.volte_sempre()
