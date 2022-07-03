class Boletim:
    def __init__(self, cod_disciplina, disciplina, professor, nota, faltas):
        self.cod_disciplina = cod_disciplina
        self.disciplina = disciplina
        self.professor = professor
        self.nota = nota
        self.faltas = faltas

    def formatBoletim(self):
        text = f'Cod_disciplina: {self.cod_disciplina}\n' + \
               f'Disciplina: {self.disciplina}\n' + \
               f'Professor: {self.professor}\n' + \
               f'Nota: {float(self.nota): .1f}\n' + \
               f'Faltas: {self.faltas}\n' + \
               '=================================================\n'

        return text
