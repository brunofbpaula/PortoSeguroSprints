import functions
import classes


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
            print("Entrando...")
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
                if escolha == "S":
                    logar(dic_usuarios)
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
    print("[1] SOLICITAR SOCORRO")
    print("[2] EDITAR SOCORRO")
    print("[3] PESQUISAR SOCORRO")
    print("[4] EXCLUIR SOCORRO")
    print("[5] VOLTAR PARA LOGIN")
    print("[6] SAIR")


def menu(dic_usuarios, nr_cpf):
    """
    Função que imprime e controla o fluxo do menu, contém todos os itens.
    :param nr_cpf: Número de CPF do usuário.
    :param dic_usuarios: Dicionário do qual será extraído as
    informações relevante do usuário para funcionamento do menu e suas respectivas funções.
    :return: None.
    """
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

        # Itens
        if escolha == "B":
            biblioteca_verde()  # BIBLIOTECA VERDE
            continue
        elif escolha == "C":
            clima(cidade)  # CLIMA E PREVISÃO
            continue
        elif escolha == "V":
            dic_usuarios, nr_cpf = area_login(dic_usuarios)  # VOLTAR AO LOGIN
            continue
        elif escolha == "R":
            recomendacao(cidade)  # RECOMENDAÇÃO DA IA
            continue
        elif escolha == "M":
            monitoramento_solo(endereco)  # INFORMAÇÕES DO SOLO
            continue
        else:
            break
    return


if __name__ == "__main__":
    dic = {}
    area_login(dic)
