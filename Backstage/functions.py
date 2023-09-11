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
        while nome != str(nome) or not re.match(r"^[A-Z][a-z]+(?: [A-Z][a-z]+)*$", nome):
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
    while True:
        dt = input("Digite sua data de nascimento: ")
        try:
            # Divide a data em fragmentos
            fragmentos = dt.split('/')

            # Confere se há três fragmentos e transforma em integer
            if len(fragmentos) == 3:
                dia, mes, ano = map(int, fragmentos)

                # Confere se o ano é válido
                if 1900 <= ano <= 2050:
                    # Formata para yyyy/mm/dd
                    dt = f"{ano:04d}/{mes:02d}/{dia:02d}"
                else:
                    print('[DATA INVÁLIDA]')
                    continue
            else:
                print('[DATA INVÁLIDA]')
                continue
        except ValueError:
            print("ERRO")
            raise ValueError
        finally:
            return dt


def nr_cpf_cliente():
    """
    Função que retorna um número de CPF no formato correto. Não há garantia da sua veracidade.
    :return: String.
    """
    print('[NÚMERO DE CPF] Da mesma forma que consta nos seus documentos oficiais. Ex: 123.456.789-10')
    cpf = input("Digite seu CPF: ")

    # Regex para CPF (não checa se é válido)
    while cpf is not re.match(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b", cpf):
        print("[DIGITE UM NÚMERO DE CPF VÁLIDO]")
        cpf = input("Digite seu número de CPF: ")
    return cpf


def email_cliente():
    print("[EMAIL] O seu melhor e-mail é o recomendado.")
    email = input("Digite o e-mail: ")

    # Regex pra e-mail
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("[DIGITE UM E-MAIL VÁLIDO]")
        email = input("Digite o e-mail: ")

    return email


def checa_senha():
    print("[SENHA] A sua senha deve conter no mínimo seis digitos.")
    senha_login = input("Digite a senha: ")
    while not re.match(r"^.{6,}$", senha_login):
        print("[DIGITE UMA SENHA VÁLIDA]")
        senha_login = input("Digite a senha: ")
    return senha_login