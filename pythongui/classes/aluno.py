class Aluno:
    def __init__(self, ra, nome, periodo):
        self.ra = ra
        self.nome = nome
        self.periodo = periodo

    def formatAluno(self):
        text = f'RA: {self.ra}\n' + \
               f'Nome: {self.nome}\n' + \
               f'Periodo: {self.periodo}\n' + \
               '==================================================\n'

        return text
