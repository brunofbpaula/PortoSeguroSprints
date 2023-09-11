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
            print("Acesse o menu fazendo login com seu e-mail e senha.")
            return dic_usuarios
        elif refazer == "R":
            print("Tudo bem! Tente novamente.")
            functions.new_line()
            continue
    return dic_usuarios


if __name__ == "__main__":
    dic = {}
    dic = cadastro(dic)
