from datetime import datetime


class Cliente:
    """
    Classe para Cliente, suas características e métodos.
    """
    def __init__(self, nome, dt_nascimento, nr_cpf, email, senha):
        self.nome = nome
        self.dt_nascimento = dt_nascimento
        self.nr_cpf = nr_cpf
        self.email = email
        self.senha = senha
        self.idade = self.calcula_idade()

    def calcula_idade(self):
        hoje = datetime.now()
        aniversario = datetime.strptime(self.dt_nascimento, '%Y-%m-%d')
        idade = hoje.year - aniversario.year - ((hoje.month, hoje.day) < (aniversario.month, aniversario.day))
        return idade

    def display(self):
        print(self.nome, self.dt_nascimento, self.idade)


if __name__ == "__main__":
    teste = Cliente('Bruno', '2004-09-29', '531.160.718-10', 'deepcooper@outlook.com', '2112121')
    teste.display()
