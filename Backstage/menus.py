def menu_login():
    """
    Função que imprime as opções de login, e retorna a escolha do usuário.
    :return: Item escolhido - String.
    """
    print("[PORTO SEGURO AUTO]")
    print("Faça login ou inscreva-se agora!")
    print("[C] Cadastro")
    print("[L] Login")
    print("[S] Sair")
    escolha = input("Escolha uma opção: ").upper().strip()
    try:
        while escolha != str(escolha) or escolha != "L" and escolha != "C" and escolha != "S":
            print("[ESCOLHA INVÁLIDA]")
            escolha = input("Escolha uma opção válida: ").upper().strip()
    finally:
        return escolha
