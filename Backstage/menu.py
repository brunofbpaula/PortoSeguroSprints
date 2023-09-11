def area_login():
    """
    Função que cadastra ou loga o usuário.
    :return: Escolha do menu.
    """
    print('[ÁREA DE LOGIN]')
    print('Logue agora para acessar nosso serviço ou cadastre-se gratuitamente.')
    print("[C] Cadastro")
    print("[L] Login")
    print("[S] Sair")
    try:
        escolha = input("Escolha uma opção: ").upper().strip()
        while escolha != str(escolha) or escolha != "L" and escolha != "C" and escolha != "S":
            print("[OPÇÃO INVÁLIDA]")
            escolha = input("Escolha uma opção válida: ").upper().strip()
    except ValueError:
        print('[ERRO]')
    finally:
        return escolha

def cadastro(dic_usuarios):
