class Usuario:
    def __init__(self, nome, senha, cpf, email, telefone):
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
        self.email = email
        self.telefone = telefone


class Horario:
    def __init__(self, horario, disponivel):
        self.horario = horario
        self.disponivel = disponivel


class Agendamento:
    def __init__(self, horario, nome, cpf, email):
        self.horario = horario
        self.nome = nome
        self.cpf = cpf
        self.email = email
