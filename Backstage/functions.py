import time as tm
import re


def new_line():
    """
    Função que pula uma linha (imprime uma em branco).
    :return: None
    """
    print()


def delay(segundos):
    """
    Função que coloca intervalos entre a execução de comandos.
    :param segundos: Quantidade de tempo do intervalo entre uma execução e outra em segundos.
    :return: Delay de X segundos.
    """
    return tm.sleep(float(segundos))


def nome_cliente():
    """
    Função que trata erros e retorna uma String.
    :return: String.
    """
    print("[NOME COMPLETO] Da mesma forma que está nos seus documentos oficiais de identificação.")
    try:
        nome = input("Digite seu nome completo: ")

        # Confere se o nome é válido
        while nome != str(nome) or not re.match(r"\b[A-Z][a-z]+([ -][A-Z][a-z]+)*\b", nome):
            print("[DIGITE UM NOME VÁLIDO]")
            nome = input("Digite seu nome completo: ")

        return nome

    except ValueError:
        print("Erro desconhecido")
        raise ValueError


def dt_nascimento_cliente():
    """
    Função que formata e retorna uma data em String.
    :return: Data de nascimento.
    """
    print("[DATA DE NASCIMENTO] No formato \'DIA/MÊS/ANO\'.")

    try:
        while True:
            dt = input("Digite sua data de nascimento: ")
            # Divide a data em fragmentos
            fragmentos = dt.split('/')

            # Confere se há três fragmentos e transforma em integer
            if len(fragmentos) == 3:
                dia, mes, ano = map(int, fragmentos)

                # Confere se o ano é válido
                if 1900 <= ano <= 2050:
                    # Formata para yyyy/mm/dd
                    dt = f"{ano:04d}-{mes:02d}-{dia:02d}"
                    return dt
                else:
                    print('[DATA INVÁLIDA]')
                    continue
            else:
                print('[DATA INVÁLIDA]')
                continue
    except ValueError:
        print("ERRO")
        raise ValueError


def nr_cpf_cliente():
    """
    Função que retorna um número de CPF no formato correto. Não há garantia da sua veracidade.
    :return: String.
    """
    print('[NÚMERO DE CPF] Da mesma forma que consta nos seus documentos oficiais. EX: 123.456.789-10.')
    cpf = input("Digite seu CPF: ")

    # Regex para CPF (não checa se é válido)
    padrao = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'
    while not re.match(padrao, cpf):
        print("[DIGITE UM NÚMERO DE CPF VÁLIDO]")
        cpf = input("Digite seu número de CPF: ")

    cpf = ''.join(filter(str.isdigit, cpf))
    return cpf


def email_cliente():
    print("[EMAIL] O seu melhor e-mail é o recomendado.")
    email = input("Digite o e-mail: ")

    # Regex pra e-mail
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("[DIGITE UM E-MAIL VÁLIDO]")
        email = input("Digite o e-mail: ")

    return email


def senha_cliente():
    print("[SENHA] A sua senha deve conter no mínimo seis digitos.")
    senha = input("Digite a senha: ")

    # Regex para senha de no mínimo seis dígitos
    while not re.match(r"^.{6,}$", senha):
        print("[DIGITE UMA SENHA VÁLIDA]")
        senha = input("Digite a senha: ")

    return senha


def tentar_novamente():
    """
    Função que imprime opção de retorno a fase anterior e retorna a escolha.
    :return: Escolha do menuzinho, String.
    """
    print("Tentar novamente?")
    print("[S] Sim")
    print("[V] Voltar")
    escolha = input("Escolha uma opção: ").upper().strip()
    while escolha != str(escolha) or escolha != "S" and escolha != "V":
        print("[ESCOLHA UMA OPÇÃO VÁLIDA]")
        escolha = input("Escolha uma opção: ").upper().strip()
    return escolha


def escolher_item():
    """
    Função para escolher um dos itens do menu principal.
    :return: Número do item escolhido.
    """
    while True:
        try:
            item_escolhido = int(input("Digite o número do item desejado: "))
            while item_escolhido > 4 or item_escolhido < 1:
                print("[OPÇÃO INVÁLIDA]")
                item_escolhido = int(input("Digite o número do item desejado: "))
            return item_escolhido

        except ValueError:
            print("[OPÇÃO INVÁLIDA]")


def confirmar():
    """
    Usado para a validação de perguntas.
    :return: Valor "SIM" (1) ou "NÃO" (2)
    """
    print("[1] SIM")
    print("[2] NÃO")
    opcao = float(input("Digite o número da opção: "))
    while opcao != 1 and opcao != 2:
        print("[OPÇÃO INVÁLIDA]")
        opcao = float(input("Digite o número da opção: "))
    return opcao


def volte_sempre():
    """
    Função que imprime uma mensagem de despedida.
    :return: None.
    """
    print("[VOLTE SEMPRE]")
    print("Até mais!")
