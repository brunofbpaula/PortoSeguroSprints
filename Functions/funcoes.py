from random import randint


# INÍCIO - BOAS VINDAS E TRATAMENTO POR NOME
def mensagem_boas_vindas():
    """
    Função que printa uma mensagem de boas-vindas.
    :return: None
    """
    print("[OLÁ]")
    print("Bem-vindo (a) ao serviço de seguro auto para veículos pesados da Porto Seguro!")
    pular_linha()


def salvar_nome_usuario():
    """
    Função que salva o nome pelo qual o usuário escolhe ser chamado enquanto o programa rodar.
    :return: Nome escolhido.
    """
    print("[A PORTO SEGURO APRECIA A SUA PREFERÊNCIA]")
    opcao = 2
    while opcao == 2:
        nome_usuario = input("Como você gostaria de ser chamado? \nMe chame de: ")
        print(f"Você escolheu ser chamado de {nome_usuario}.")
        print("O nome digitado acima está correto?")
        opcao = confirmar()
        if opcao == 2:
            print("Tudo bem! Tente novamente.")
            pular_linha()
        else:
            pular_linha()
            return nome_usuario


def mensagem_erro():
    """
    Função que printa uma mensagem de erro.
    :return: None
    """
    print("SELECIONE UMA OPÇÃO VÁLIDA.")


# UTILIDADES


def pular_linha():
    """
    Função que printa uma linha vazia.
    :return: None
    """
    print()


def confirmar():
    """
    Usado para a validação de perguntas.
    :return: Valor "SIM" (1) ou "NÃO" (2)
    """
    print("[1] SIM")
    print("[2] NÃO")
    opcao = float(input("Digite o número da opção: "))
    while opcao != 1 and opcao != 2:
        mensagem_erro()
        opcao = float(input("Digite o número da opção: "))
    return opcao


# MENU


def itens_menu(nome):
    """
    Função que printa os itens do menu principal.
    :param nome: Nome do usuário, escolhido pelo próprio anteriormente.
    :return: None
    """
    print("[MENU PRINCIPAL]")
    print(f"{nome}, por favor, selecione um dos itens abaixo: ")
    print("[1] SOLICITAR SOCORRO")
    print("[2] EDITAR SOCORRO")
    print("[3] PESQUISAR SOCORRO")
    print("[4] EXCLUIR SOCORRO")
    print("[5] SAIR")


def escolher_item():
    """
    Função para escolher um dos itens do menu principal.
    :return: Número do item escolhido.
    """
    item_escolhido = float(input("Digite o número do item desejado: "))
    while item_escolhido != int(item_escolhido) or item_escolhido > 5 or item_escolhido < 1:
        mensagem_erro()
        item_escolhido = float(input("Digite o número do item desejado: "))
    return item_escolhido


def menu_principal(nome):
    """
    Função que une todos os itens do menu.
    :param nome: Nome pelo qual o usuário escolher ser chamado anteriormente.
    :return: None
    """
    itens_menu(nome)
    item = escolher_item()
    sinistros = {}
    while True:
        if item == 1:
            item_um(nome, sinistros)
            itens_menu(nome)
            item = escolher_item()
        elif item == 2:
            pular_linha()
            print("[EDITAR SOCORRO]")
            print("EM MANUTENÇÃO. TENTE NOVAMENTE MAIS TARDE.")
            pular_linha()
            itens_menu(nome)
            item = escolher_item()
        elif item == 3:
            pular_linha()
            item_tres(sinistros)
            itens_menu(nome)
            item = escolher_item()
        elif item == 4:
            pular_linha()
            item_quatro(sinistros)
            itens_menu(nome)
            item = escolher_item()
        elif item == 5:
            pular_linha()
            print("[VOLTE SEMPRE]")
            print("A Porto Seguro está à sua disposição.")
            break
        else:
            print("ERRO INESPERADO")
            break


# ITEM UM - SOLICITAR SOCORRO
# CONFIRMAÇÃO DO CONTRATO - FINALIZADO
# INFORMAÇÕES DO VEÍCULO - FINALIZADO
# INFORMAÇÕES DA CARGA - PLANEJANDO
# PROBLEMA DO VEÍCULO - EM ANDAMENTO
# ENDEREÇO DA OCORRÊNCIA - FINALIZADO


# CONFIRMAÇÃO DO CONTRATO
def confirmacao_contrato(nome):
    """
    Função que captura alguns dados do contrato do segurado como nome completo, CPF e número de apólice.
    :return: Lista com informações do contrato.
    """
    opcao = 2
    while opcao == 2:
        print("[SOLICITAÇÃO DE SOCORRO - CONFIRMAÇÃO DE CONTRATO]")
        print("Por favor, preencha os dados presentes em seu contrato abaixo.")
        nome_completo = input("Digite o seu nome completo: ")
        cpf = validar_cpf()
        apolice = input("Digite o número da sua apólice: ")
        contrato_puro = [nome_completo, cpf, apolice]
        contrato = [f"Responsável: {nome_completo}", f"CPF do Responsável: {cpf}", f"Número de Apólice: {apolice}"]
        pular_linha()
        print("[CONFIRMAÇÃO]")
        print(f"{nome}, você digitou que seu nome completo é {nome_completo}, e seu CPF {cpf}. "
              f"\nO número da sua apólice é {apolice}.")
        print("Os dados acima estão corretos?")
        opcao = confirmar()
        if opcao == 1:
            return contrato, contrato_puro
        if opcao == 2:
            print("Tudo bem. Preencha os dados novamente.")
            pular_linha()


def validar_cpf():
    """
    Função para validar CPF, ainda em manutenção.
    :return: Valor de CPF válido.
    """
    cpf = input("Número de CPF: ")
    return cpf


# INFORMAÇÕES DO MODELO DO VEÍCULO
def caracteristicas_veiculo(nome):
    """
    Função que capta os dados do veículo do sinistro.
    :param nome: Nome pelo qual o usúario escolher ser chamado anteriormente.
    :return: Lista concatenada e Lista "pura".
    """
    opcao = 2
    while opcao == 2:
        print("[SOLICITAÇÃO DE SOCORRO - CARACTERÍSTICAS GERAIS DO VEÍCULO]")
        print("Por favor, preencha os dados do seu veículo abaixo.")
        marca = input("Digite a marca do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        ano_veiculo = input("Digite o ano do veículo: ")
        placa_veiculo = input("Digite a placa do veículo assegurado: ")
        peso_veiculo = float(input("Digite o peso do veículo em toneladas: "))
        altura_veiculo = float(input("Digite a altura do veículo em metros: "))
        pular_linha()
        print("[SOLICITAÇÃO DE SOCORRO - CARACTERÍSTICAS DA CARROCERIA]")
        print("Por favor, preencha os dados da carroceria do seu veículo abaixo.")
        chassi = input("Digite o chassi do veículo: ")
        eixos = int(input("Digite a quantidade de eixos do veículo: "))
        combustivel = float(input("Digite a capacidade de combustível máxima do veículo em litros: "))
        veiculo_puro = [marca, modelo, ano_veiculo, placa_veiculo, chassi, eixos,
                        altura_veiculo, peso_veiculo, combustivel]
        veiculo = [f"Marca: {marca}", f"Modelo: {modelo}", f"Ano: {ano_veiculo}", f"Placa: {placa_veiculo}",
                   f"Altura em metros: {altura_veiculo}", f"Peso em toneladas: {peso_veiculo}"
                   f"Chassi: {chassi}", f"Eixos: {eixos}", f"Combustível Máximo em litros: {combustivel}"]
        pular_linha()
        print("[CONFIRMAÇÃO]")
        print(f"{nome}, você digitou que seu veículo é um(a) {marca} {modelo} {ano_veiculo}, placa {placa_veiculo}."
              f"\nO veículo têm {altura_veiculo:.2f} metros de altura e pesa {peso_veiculo} toneladas."
              f"\nA carroceria possui um chassi {chassi} e {eixos} eixos."
              f"\nO combustível máximo que o veículo pode conter é {combustivel} litros.")
        print("Os dados acima estão corretos?")
        opcao = confirmar()
        if opcao == 1:
            return veiculo, veiculo_puro
        if opcao == 2:
            print("Tudo bem. Preencha os dados novamente.")
            pular_linha()


# PROBLEMA DO VEÍCULO
def problema_veiculo(nome):
    """
    Função que capta o problema do veículo.
    :param nome: Nome pelo qual o usúario escolher ser chamado anteriormente.
    :return: Lista concatenada e lista "pura".
    """
    opcao = 2
    while opcao == 2:
        print("[SOLICITAÇÃO DE SOCORRO - SINISTRO]")
        menu_problema(nome)
        problema_escolhido = escolher_problema()
        problema = [f"Problema: {problema_escolhido}"]
        problema_puro = [problema]
        return problema, problema_puro


# SINISTROS
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
    problema_escolhido = float(input("Digite o número do sinistro: "))
    while problema_escolhido != int(problema_escolhido) or problema_escolhido > 5 or problema_escolhido < 1:
        mensagem_erro()
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


# ENDEREÇO DA OCORRÊNCIA
def localizacao_veiculo(nome):
    """
    Função que capta os dados do endereço do sinistro.
    :param nome: Nome pelo qual o usúario escolher ser chamado anteriormente.
    :return: Lista concatenada e lista "pura".
    """
    opcao = 2
    while opcao == 2:
        print("[SOLICITAÇÃO DE SOCORRO - LOCALIZAÇÃO DO VEÍCULO]")
        print("Preencha os dados da localização atual do véiculo abaixo.")
        rua = input("Nome da rua: ")
        numero_rua = int(input("Número da rua: "))
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        localizao_pura = [rua, numero_rua, cidade, estado]
        localizacao = [f"Rua: {rua}", f"Número: {numero_rua}", f"Cidade: {cidade}", f"Estado: {estado}"]
        pular_linha()
        print("[CONFIRMAÇÃO]")
        print(f"{nome}, você digitou que a atual localização do veículo é: {rua} nº {numero_rua}, "
              f"{cidade} - {estado}.")
        print("Os dados acima estão corretos?")
        opcao = confirmar()
        if opcao == 1:
            return localizacao, localizao_pura
        if opcao == 2:
            print("Tudo bem. Preencha os dados novamente.")
            pular_linha()


# RESUMO OCORRÊNCIA
def resumo_sinistro(sinistros, numero):
    """
    Função que printa um resumo da ocorrência de sinistro.
    :param sinistros: Dicionário de sinistros.
    :param numero: Número do sinistro, chave de dicionário.
    :return: None
    """
    print(f"[DADOS DA OCORRÊNCIA - Nº {numero}]")
    print("[ASSEGURADO]")
    print(sinistros[numero]["Contrato"][0])  # Responsável
    print(sinistros[numero]["Contrato"][1])  # CPF
    print("[VEÍCULO]")
    print(sinistros[numero]["Veículo"][0])  # Marca
    print(sinistros[numero]["Veículo"][1])  # Modelo
    print(sinistros[numero]["Veículo"][2])  # Ano
    print(sinistros[numero]["Veículo"][3])  # Placa
    print("[SINISTRO DA OCORRÊNCIA]")
    print(sinistros[numero]["Problema"][0])  # Sinistro
    print("Guincho enviado: EM ANÁLISE")  # Guincho
    print("[LOCALIZAÇÃO ATUAL DO VEÍCULO]")
    print(sinistros[numero]["Localização"][0])  # Rua
    print(sinistros[numero]["Localização"][1])  # Número
    print(sinistros[numero]["Localização"][2])  # Cidade
    print(sinistros[numero]["Localização"][3])  # Estado


# FUNÇÃO ITEM UM
def item_um(nome, sinistros):
    """
    Função para ativar o processo inteiro de solicitar socorro.
    :param nome: Nome pelo qual o usuário escolher ser chamado anteriormente.
    :param sinistros: Dicionário em que o sinistro será armazenado.
    :return: Novo valor
    """
    sinistro_puro = {}
    print(f"Vamos atender o seu socorro, {nome}. Mas antes, por favor, nos informe alguns dados.")
    pular_linha()
    contrato, contrato_puro = confirmacao_contrato(nome)
    pular_linha()
    veiculo, veiculo_puro = caracteristicas_veiculo(nome)
    pular_linha()
    localizacao, localizacao_pura = localizacao_veiculo(nome)
    pular_linha()
    problema, problema_puro = problema_veiculo(nome)
    pular_linha()
    numero_protocolo = randint(10000000000, 99999999999)
    sinistro_puro[numero_protocolo] = {"Contrato Puro": contrato_puro, "Veículo Puro": veiculo_puro,
                                       "Localização Pura": localizacao_pura, "Problema Puro": problema_puro}
    sinistros[numero_protocolo] = {"Contrato": contrato, "Veículo": veiculo, "Localização": localizacao,
                                   "Problema": problema}
    resumo_sinistro(sinistros, numero_protocolo)
    pular_linha()
    print("[GUINCHO A CAMINHO!]")
    print("A ocorrência foi realizada. Você pode checar as informações do sinistro "
          f"no menu através do número de protocolo {numero_protocolo}.")
    pular_linha()
    return sinistros


# FUNÇÃO ITEM TRÊS
def item_tres(sinistros):
    """
    Função para pesquisar sinistro.
    :param sinistros: Dicionário com todos os sinistros.
    :return: None
    """
    print("[PESQUISADOR DE SINISTRO]")
    numero_sinistro = int(input("Digite o número do sinistro que você deseja pesquisar: "))
    sinistro_pesquisado = sinistros.get(numero_sinistro)
    if sinistro_pesquisado is not None:
        print(f"O sinistro {numero_sinistro} foi encontrado!")
        pular_linha()
        resumo_sinistro(sinistros, numero_sinistro)
    else:
        print(f"O sinistro {numero_sinistro} não foi encontrado.")
    pular_linha()


# FUNÇÃO ITEM QUATRO
def item_quatro(sinistros):
    """
    Função que deleta sinistros existentes no dicionário de sinistros.
    :param sinistros: Dicionário de sinistros.
    :return: None
    """
    print("[EXCLUIR SOCORRO]")
    print("Atenção. O sinistro digitado será permanentemente deletado.")
    print("Prosseguir mesmo assim?")
    opcao = confirmar()
    if opcao == 1:
        numero_sinistro = int(input("Digite o número do sinistro: "))
        sinistro_pesquisado = sinistros.get(numero_sinistro)
        if sinistro_pesquisado is not None:
            del sinistros[numero_sinistro]
            print(f"O sinistro {numero_sinistro} foi deletado.")
        else:
            print(f"O sinistro {numero_sinistro} não foi encontrado.")
    else:
        print("Voltando ao menu...")
    pular_linha()
