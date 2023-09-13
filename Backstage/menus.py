import functions
import classes
from random import randint


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


def area_login(dic_usuarios):
    while True:
        escolha = menu_login()
        if escolha == "S":
            chave_vazia = None  # Chave sem valor, entra na condicional do menu que retorna (para) a função.
            return dic_usuarios, chave_vazia
        elif escolha == "C":
            functions.new_line()
            cadastro(dic_usuarios)  # Dicionário atualizado
            functions.new_line()
            continue
        elif escolha == "L":
            functions.new_line()
            chave_dic = logar(dic_usuarios)  # Chave valorada, parâmetro da função menu
            functions.new_line()
            if chave_dic is not None:
                return dic_usuarios, chave_dic
            else:
                continue
        else:
            print("Oops!")  # Nunca vai executar... eu acho.
            return


def cadastro(dic_usuarios):
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
        usuario = classes.Cliente(nome, dt_nascimento, nr_cpf, email, senha)
        dic_usuarios[nr_cpf] = usuario
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
            print("[TUDO CERTO]")
            print("Salvando...")
            functions.delay(1)
            print("Acesse o menu fazendo login com CPF e SENHA.")
            functions.delay(1)
            return dic_usuarios
        elif refazer == "R":
            print("Tudo bem! Tente novamente.")
            functions.new_line()
            continue
    return dic_usuarios


def logar(dic_usuarios):
    """
    Função que loga o usuário, validando CPF e senha.
    :param dic_usuarios: Dicionário com todos os usuários, com a chave sendo o CPF.
    :return: Chave do dicionário.
    """
    while True:
        print("[ÁREA DE LOGIN]")

        # Procura a chave no dicionário
        nr_cpf = input("Digite o seu CPF: ")
        validacao_email = dic_usuarios.get(nr_cpf)

        # Se não achar, dá a opção de tentar novamente ou sair
        if validacao_email is None:
            print("[CPF NÃO ENCONTRADO]")
            escolha = functions.tentar_novamente()
            if escolha == "S":
                functions.new_line()
                continue
            else:
                break

        # Se achar, verifica se a senha é a mesma digitada
        else:
            senha_login = input("Digite a sua senha: ")
            valida_senha = dic_usuarios[nr_cpf]

            # Loga o usuário
            if valida_senha.senha == senha_login:
                functions.delay(0.5)
                functions.new_line()
                print("Entrando...")
                functions.delay(1)
                return nr_cpf

            # Outra tentativa ou sair
            else:
                print("[SENHA INCORRETA]")
                escolha = functions.tentar_novamente()
                functions.new_line()
                if escolha == "S":
                    continue
                else:
                    break


def itens_menu(nome):
    """
    Função que printa os itens do menu principal.
    :param nome: Nome do usuário.
    :return: None
    """
    print("[MENU PRINCIPAL]")
    print(f"{nome}, por favor, selecione um dos itens abaixo: ")
    print("[1] AVISAR SINISTRO")
    print("[2] EDITAR AVISO DE SINISTRO")
    print("[3] PESQUISAR AVISO DE SINISTRO")
    print("[4] EXCLUIR AVISO DE SINISTRO")
    print("[5] VOLTAR PARA LOGIN")
    print("[6] SAIR")


def menu(dic_usuarios, nr_cpf):
    """
    Função que imprime e controla o fluxo do menu, contém todos os itens.
    :param nr_cpf: Número de CPF do usuário.
    :param dic_usuarios: Dicionário do qual será extraído as
    informações relevante do usuário para funcionamento do menu e as suas funções.
    :return: None.
    """
    sinistros = {}
    while True:

        # Se a chave não tem valor, o usuário escolheu sair
        if nr_cpf is None:
            functions.new_line()
            return

        # Nome do usuário
        nome = dic_usuarios[nr_cpf].nome.split(" ")[0]

        # Escolhendo item do menu
        itens_menu(nome)
        escolha = functions.escolher_item()  # ITEM ESCOLHIDO PELO USUÁRIO
        functions.new_line()

        # Itens do menu

        # Avisar sinistro
        if escolha == 1:
            aviso_sinistro(nome, sinistros)
            continue

        # Editar aviso de sinistro
        elif escolha == 2:
            print("[EDITAR AVISO DE SINISTRO]")
            print("EM MANUTENÇÃO. TENTE NOVAMENTE MAIS TARDE.")
            functions.new_line()
            functions.delay(3)
            continue

        # Pesquisar aviso de sinistro
        elif escolha == 3:
            pesquisar_sinistro(dic_usuarios, nr_cpf, sinistros)
            continue

        # Excluir aviso de sinistro
        elif escolha == 4:
            excluir_sinistro(sinistros)
            continue

        # Voltar para o login
        elif escolha == 5:
            dic_usuarios, nr_cpf = area_login(dic_usuarios)
            continue

        # Sair do menu
        else:
            break
    return


# ITENS DO MENU
def aviso_sinistro(nome, sinistros):
    """
    Função para ativar o processo inteiro de aviso de sinistro.
    :param nome: Nome do usuário.
    :param sinistros: Dicionário em que o sinistro será armazenado.
    :return: Novo valor do dicionário.
    """
    print("[AVISAR SINISTRO]")
    print(f"Vamos atender o seu socorro, {nome}. Mas antes, por favor, nos informe alguns dados.")
    functions.new_line()
    functions.delay(0.5)
    opcao = 2
    while opcao == 2:

        # Dados inseridos nas tabelas contrato e veículo
        print("[AVISO DE SINISTRO - VEÍCULO]")
        print("Por favor, preencha os dados presentes em seu contrato abaixo.")
        apolice = input("Digite o número da sua apólice: ")
        marca = input("Digite a marca do veículo: ")
        modelo = input("Digite o modelo do veículo: ")

        # Não-String
        try:
            ano_veiculo = int(input("Digite o ano do veículo: "))
        except ValueError:
            while True:
                print('[ANO INVÁLIDO]')
                ano_veiculo = int(input("Digite o ano do veículo: "))
                if type(ano_veiculo) == int:
                    break
                else:
                    continue

        placa_veiculo = input("Digite a placa do veículo assegurado: ")
        nr_chassi = input("Digite o número do chassi do veículo: ")

        # Lista de dados do veículo e contrato
        dados = [apolice, marca, modelo, ano_veiculo, placa_veiculo, nr_chassi]
        functions.delay(1)
        functions.new_line()

        # Dados inseridos na tabela do local do sinistro
        print("[AVISO DE SINISTRO - LOCALIZAÇÃO DO VEÍCULO]")
        print("Preencha os dados da localização atual do véiculo abaixo.")
        rua = input("Nome da rua: ")

        # Não-String
        try:
            numero_rua = int(input("Número da rua: "))
        except ValueError:
            while True:
                print('[ANO INVÁLIDO]')
                numero_rua = int(input("Número da rua: "))
                if type(numero_rua) == int:
                    break
                else:
                    continue

        cidade = input("Cidade: ")
        estado = input("Estado: ")

        # Lista de dados do local do sinistro
        localizacao = [rua, numero_rua, cidade, estado]
        functions.new_line()
        functions.delay(1)

        print('[AVISO DE SINISTRO - PROBLEMA DA OCORRÊNCIA]')
        menu_problema(nome)
        problema = escolher_problema()
        functions.new_line()
        functions.delay(1)

        # Mudar condição de loop
        print("[CONFIRME AS INFORMAÇÕES PASSADAS]")
        print("Todos os dados estão corretos?")
        opcao = functions.confirmar()

        # Para loop
        if opcao == 1:

            # Chave do sinistro
            numero_protocolo = randint(100000, 999999)
            # Atualiza dicionário
            sinistros[numero_protocolo] = {"Dados": dados, "Localização": localizacao, "Problema": problema}
            functions.new_line()
            print("[GUINCHO A CAMINHO!]")
            print("A ocorrência foi realizada. Você pode checar as informações do sinistro "
                  f"no menu através do número de protocolo {numero_protocolo}.")
            functions.new_line()
            print("Voltando ao menu...")
            functions.delay(5)
            break

        # Refaz
        if opcao == 2:
            print("Tudo bem. Preencha os dados novamente.")

    functions.new_line()
    return sinistros


# FUNÇÃO ITEM TRÊS
def pesquisar_sinistro(dic_usuarios, nr_cpf, sinistros):
    """
    Função para pesquisar sinistro.
    :param nr_cpf: Número de CPF chave de dicionário.
    :param dic_usuarios: Dicionário de usuários.
    :param sinistros: Dicionário com todos os sinistros.
    :return: None
    """
    print("[PESQUISADOR DE SINISTRO]")
    numero_sinistro = int(input("Digite o número do sinistro que você deseja pesquisar: "))
    sinistro_pesquisado = sinistros.get(numero_sinistro)
    if sinistro_pesquisado is not None:
        print(f"O sinistro {numero_sinistro} foi encontrado!")
        functions.new_line()
        functions.delay(2)
        resumo_sinistro(dic_usuarios, nr_cpf, sinistros, numero_sinistro)
        functions.new_line()
        print("Voltando ao menu...")
        functions.delay(10)
    else:
        print(f"O sinistro {numero_sinistro} não foi encontrado.")
    functions.new_line()


# FUNÇÃO ITEM QUATRO
def excluir_sinistro(sinistros):
    """
    Função que deleta sinistros existentes no dicionário de sinistros.
    :param sinistros: Dicionário de sinistros.
    :return: None
    """
    print("[EXCLUIR SOCORRO]")
    print("Atenção. O sinistro digitado será permanentemente deletado.")
    print("Prosseguir mesmo assim?")
    opcao = functions.confirmar()
    if opcao == 1:
        numero_sinistro = int(input("Digite o número do sinistro: "))
        sinistro_pesquisado = sinistros.get(numero_sinistro)
        if sinistro_pesquisado is not None:
            del sinistros[numero_sinistro]
            print(f"O sinistro {numero_sinistro} foi deletado.")
            functions.new_line()
            print("Voltando ao menu...")
            functions.delay(5)
        else:
            print(f"O sinistro {numero_sinistro} não foi encontrado.")
    else:
        print("Voltando ao menu...")
    functions.new_line()


def menu_problema(nome):
    """
    Função que printa o menu para escolha de sinistro (problema).
    :param nome: Nome pelo qual o usúario escolher ser chamado anteriormente.
    :return: None
    """
    print(f"{nome}, por favor, selecione o item que melhor descreve o sinistro.")
    print("[1] PANE")
    print("[2] COLISÃO")
    print("[3] INCÊNDIO")
    print("[4] TOMBAMENTO")
    print("[5] DESASTRE NATURAL")


# ESCOLHER SINISTRO
def escolher_problema():
    """
    Função para escolher um dos itens do menu de sinistros.
    :return: Variável do problema em String.
    """
    problema_escolhido = float(input("Digite o número do problema: "))
    while problema_escolhido != int(problema_escolhido) or problema_escolhido > 5 or problema_escolhido < 1:
        print('[OPÇÃO INVÁLIDA]')
        problema_escolhido = float(input("Digite o número do sinistro: "))
    if problema_escolhido == 1:
        problema_escolhido = "PANE"
    elif problema_escolhido == 2:
        problema_escolhido = "COLISÃO"
    elif problema_escolhido == 3:
        problema_escolhido = "INCÊNDIO"
    elif problema_escolhido == 4:
        problema_escolhido = "TOMBAMENTO"
    else:
        problema_escolhido = "DESASTRE NATURAL"
    return problema_escolhido


def resumo_sinistro(dic_usuarios, nr_cpf, sinistros, numero):
    """
    Função que printa um resumo da ocorrência de sinistro.
    :param nr_cpf: Número de CPF, chave de dicionário.
    :param dic_usuarios: Dicionário de usuários.
    :param sinistros: Dicionário de sinistros.
    :param numero: Número do sinistro, chave de dicionário.
    :return: None
    """
    marca = sinistros[numero]['Dados'][1]
    modelo = sinistros[numero]['Dados'][2]
    ano = sinistros[numero]['Dados'][3]
    placa = sinistros[numero]['Dados'][4]

    rua = sinistros[numero]["Localização"][0]
    nr_rua = sinistros[numero]["Localização"][1]
    cidade = sinistros[numero]["Localização"][2]
    estado = sinistros[numero]["Localização"][3]

    print(f"[AVISO DE SINISTRO Nº {numero}]")

    # Contrato
    print("[ASSEGURADO]")
    print(f'Nome: {dic_usuarios[nr_cpf].nome}')
    print(f'Número de CPF: {nr_cpf}')

    # Veículo
    print("[VEÍCULO DO SINISTRO]")
    print(f'Modelo: {marca} {modelo} {ano}')
    print(f"Placa: {placa}")

    # Sinistro
    print("[SINISTRO DA OCORRÊNCIA]")
    print(sinistros[numero]["Problema"])  # Sinistro

    # Local do Sinistro
    print("[LOCALIZAÇÃO ATUAL DO VEÍCULO]")
    print(f'{rua} {nr_rua} {cidade} {estado}')


if __name__ == "__main__":
    mensagem_boas_vindas()
    dic = {}
    dic, cpf = area_login(dic)
    menu(dic, cpf)
    functions.volte_sempre()
