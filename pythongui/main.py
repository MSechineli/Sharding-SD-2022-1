import grpc
import faculdade_pb2  # Funções de marshalling e unmarshalling
import faculdade_pb2_grpc
import PySimpleGUI as sg
from classes import aluno, boletim

sg.theme_global('DarkBlue3')


def windowSelectOp():
    # All the stuff inside your window.
    layout = [
        [sg.Text('Informe qual operação deseja realizar:')],
        [sg.Radio('Inserir na tabela Matrícula', 'operacao', key='1')],
        [sg.Radio('Alterar notas na tabela Matrícula', 'operacao', key='2')],
        [sg.Radio('Alterar faltas na tabela Matrícula', 'operacao', key='3')],
        [sg.Radio('Listagem de alunos', 'operacao', key='4')],
        [sg.Radio('Boletim', 'operacao', key='5')],
        [sg.Push(), sg.Button('Escolher operacao'), sg.Button('Encerrar'), sg.Push()]
    ]

    # Create the Window
    window = sg.Window('Projeto com Shardingsphere', layout, size=(350, 200))

    event, values = window.read()

    return window, event, values


def windowsFirstOp(stub):
    # All the stuff inside your window.
    layout = [
        [sg.Text('Preencha os dados:')],
        [sg.Push(), sg.Text('Informe o RA:'), sg.Input(size=(12, 0), key='ra')],
        [sg.Push(), sg.Text('Informe o cod_disciplina:'), sg.Input(size=(12, 0), key='cod_disciplina')],
        [sg.Push(), sg.Text('Informe o ano:'), sg.Input(size=(12, 0), key='ano')],
        [sg.Push(), sg.Text('Informe o semestre:'), sg.Input(size=(12, 0), key='semestre')],
        [sg.Push(), sg.Button('Enviar'), sg.Button('Cancelar'), sg.Push()]
    ]

    # Create the Window
    window = sg.Window('Inserir nova matrícula', layout)

    event, values = window.read()

    if event == 'Enviar':
        # Preenche a estrutura da matricula, porém com as notas e faltas com o valor padrao 0;
        matricula = faculdade_pb2.Matricula()
        matricula.ra = int(values['ra'])
        matricula.cod_disciplina = str(values['cod_disciplina'])
        matricula.ano = int(values['ano'])
        matricula.semestre = int(values['semestre'])
        matricula.nota = 0
        matricula.faltas = 0

        # Realiza uma chamada na funcao de inserir matricula e recebe uma resposta do servidor;
        resposta = stub.InserirMatricula(matricula)

        # Recebe a resposta do servidor
        sg.popup(f'Servidor: {resposta.mensagem}')

    elif event == sg.WIN_CLOSED or event == 'Cancelar':
        pass

    window.close()


def windowsSecondOp(stub):
    # All the stuff inside your window.
    layout = [
        [sg.Text('Preencha os dados:')],
        [sg.Push(), sg.Text('Informe o RA:'), sg.Input(size=(12, 0), key='ra')],
        [sg.Push(), sg.Text('Informe o cod_disciplina:'), sg.Input(size=(12, 0), key='cod_disciplina')],
        [sg.Push(), sg.Text('Informe o ano:'), sg.Input(size=(12, 0), key='ano')],
        [sg.Push(), sg.Text('Informe o semestre:'), sg.Input(size=(12, 0), key='semestre')],
        [sg.Push(), sg.Text('Informe a nota:'), sg.Input(size=(12, 0), key='nota')],
        [sg.Push(), sg.Button('Enviar'), sg.Button('Cancelar'), sg.Push()]
    ]

    # Create the Window
    window = sg.Window('Alterar nota de uma matrícula', layout)

    event, values = window.read()

    if event == 'Enviar':
        # Preenche a estrutura da matricula, porém, enviando tambem o campo "nota";
        matricula = faculdade_pb2.Matricula()
        matricula.ra = int(values['ra'])
        matricula.cod_disciplina = str(values['cod_disciplina'])
        matricula.ano = int(values['ano'])
        matricula.semestre = int(values['semestre'])
        matricula.nota = float(values['nota'])

        # Realiza uma chamada na funcao de atualizar nota da matricula e recebe uma resposta do servidor;
        resposta = stub.AtualizarNota(matricula)

        # Recebe a resposta do servidor
        sg.popup(f'Servidor: {resposta.mensagem}')

    elif event == sg.WIN_CLOSED or event == 'Cancelar':
        pass

    window.close()


def windowsThirdOp(stub):
    # All the stuff inside your window.
    layout = [
        [sg.Text('Preencha os dados:')],
        [sg.Push(), sg.Text('Informe o RA:'), sg.Input(size=(12, 0), key='ra')],
        [sg.Push(), sg.Text('Informe o cod_disciplina:'), sg.Input(size=(12, 0), key='cod_disciplina')],
        [sg.Push(), sg.Text('Informe o ano:'), sg.Input(size=(12, 0), key='ano')],
        [sg.Push(), sg.Text('Informe o semestre:'), sg.Input(size=(12, 0), key='semestre')],
        [sg.Push(), sg.Text('Informe as faltas:'), sg.Input(size=(12, 0), key='faltas')],
        [sg.Push(), sg.Button('Enviar'), sg.Button('Cancelar'), sg.Push()]
    ]

    # Create the Window
    window = sg.Window('Alterar faltas de uma matrícula', layout)

    event, values = window.read()

    if event == 'Enviar':
        # Preenche a estrutura da matricula, porém, enviando tambem o campo "faltas";
        matricula = faculdade_pb2.Matricula()
        matricula.ra = int(values['ra'])
        matricula.cod_disciplina = str(values['cod_disciplina'])
        matricula.ano = int(values['ano'])
        matricula.semestre = int(values['semestre'])
        matricula.faltas = int(values['faltas'])

        # Realiza uma chamada na funcao de atualizar faltas da matricula e recebe uma resposta do servidor;
        resposta = stub.AtualizarFaltas(matricula)

        # Recebe a resposta do servidor
        sg.popup(f'Servidor: {resposta.mensagem}')

    elif event == sg.WIN_CLOSED or event == 'Cancelar':
        pass

    window.close()


def windowOutput(lista, op):
    layout = [
        [sg.Output(size=(80, 40), key='output', font=('Default', 10))],
        [sg.Push(), sg.Button('Show Results'), sg.Button('Exit'), sg.Push()]
    ]

    window = sg.Window('Listagem', layout)

    text = None

    if op == 4:
        text = '==================== Lista de alunos ====================\n'
        for student in lista:
            text += student.formatAluno()
    elif op == 5:
        text = '==================== Boletim ====================\n'
        for discipline in lista:
            text += discipline.formatBoletim()

    while True:  # Event Loop
        event, values = window.Read()
        window.Element('output').Update(text)
        if event is None or event == 'Exit':
            break

    window.Close()


def windowsFourthOp(stub):
    # All the stuff inside your window.
    layout = [
        [sg.Text('Preencha os dados:')],
        [sg.Push(), sg.Text('Informe o cod_disciplina:'), sg.Input(size=(12, 0), key='cod_disciplina')],
        [sg.Push(), sg.Text('Informe o ano:'), sg.Input(size=(12, 0), key='ano')],
        [sg.Push(), sg.Text('Informe o semestre:'), sg.Input(size=(12, 0), key='semestre')],
        [sg.Push(), sg.Button('Enviar'), sg.Button('Cancelar'), sg.Push()]
    ]

    # Create the Window
    window = sg.Window('Listar alunos de uma disciplina', layout)

    # window.write_event_value()
    event, values = window.read()

    if event == 'Enviar':
        # Preenche a estrutura da matricula enviando apenas: codigo da disciplina, ano e semestre;
        matricula = faculdade_pb2.Matricula()
        matricula.cod_disciplina = str(values['cod_disciplina'])
        matricula.ano = int(values['ano'])
        matricula.semestre = int(values['semestre'])

        # Realiza uma chamada na funcao de listar alunos de uma disciplina e recebe uma resposta do servidor;
        resposta = stub.ListarAlunosDaDisciplina(matricula)

        # Quantidade de alunos
        qtdAlunos = len(resposta.alunos)

        if qtdAlunos == 0:
            # Recebe a resposta do servidor
            sg.popup('Servidor: Não há alunos!')
        else:

            # Cria lista de alunos
            listaAlunos = []

            print(f"QUANTIDADE: {qtdAlunos}")

            for student in resposta.alunos:
                listaAlunos.append(
                    aluno.Aluno(
                        str(student.ra),
                        student.nome,
                        str(student.periodo)
                    )
                )

            windowOutput(listaAlunos, 4)

    elif event == sg.WIN_CLOSED or event == 'Cancelar':
        pass

    window.close()


def windowsFifthOp(stub):
    # All the stuff inside your window.
    layout = [
        [sg.Text('Preencha os dados:')],
        [sg.Push(), sg.Text('Informe o RA:'), sg.Input(size=(12, 0), key='ra')],
        [sg.Push(), sg.Text('Informe o ano:'), sg.Input(size=(12, 0), key='ano')],
        [sg.Push(), sg.Text('Informe o semestre:'), sg.Input(size=(12, 0), key='semestre')],
        [sg.Push(), sg.Button('Enviar'), sg.Button('Cancelar'), sg.Push()]
    ]

    # Create the Window
    window = sg.Window('Listar alunos de uma disciplina', layout)

    # window.write_event_value()
    event, values = window.read()

    if event == 'Enviar' or event == sg.CLOSE:
        # Preenche a estrutura da matricula enviando apenas: ra, ano e semestre;
        matricula = faculdade_pb2.Matricula()
        matricula.ra = int(values['ra'])
        matricula.ano = int(values['ano'])
        matricula.semestre = int(values['semestre'])

        # Realiza uma chamada na funcao de listar o boletim de um aluno e recebe uma resposta do servidor;
        resposta = stub.ListarBoletimDoAluno(matricula)

        # Quantidade de disciplinas
        qtdDisciplinas = len(resposta.disciplina)

        if qtdDisciplinas == 0:
            # Recebe a resposta do servidor
            sg.popup('Servidor: Não há disciplinas!')
        else:
            # Cria lista de disciplinas
            listaDisciplinas = []

            print(f"QUANTIDADE: {qtdDisciplinas}")
            for index, _ in enumerate(resposta.disciplina):
                listaDisciplinas.append(
                    boletim.Boletim(
                        resposta.disciplina[index].codigo,
                        resposta.disciplina[index].nome,
                        resposta.disciplina[index].professor,
                        resposta.matricula[index].faltas,
                        resposta.matricula[index].faltas
                    )
                )

            windowOutput(listaDisciplinas, 5)

    elif event == sg.WIN_CLOSED or event == 'Cancelar':
        pass

    window.close()


def mainWindow(stub):
    while True:
        # Event Loop to process "events" and get the "values" of the inputs
        window, event, values = windowSelectOp()
        if event == sg.WIN_CLOSED or event == 'Encerrar':  # if user closes window or clicks cancel
            break

        if event == 'Escolher operacao':
            if values['1']:
                print('Operacao selecionada: Inserir na tabela Matrícula')
                windowsFirstOp(stub)
            elif values['2']:
                print('Operacao selecionada: Alterar notas na tabela Matrícula')
                windowsSecondOp(stub)
            elif values['3']:
                print('Operacao selecionada: Alterar faltas na tabela Matrícula')
                windowsThirdOp(stub)
            elif values['4']:
                print('Operacao selecionada: Listagem de alunos')
                windowsFourthOp(stub)
            elif values['5']:
                print('Operacao selecionada: Boletim')
                windowsFifthOp(stub)

        window.close()


if __name__ == '__main__':
    # Cria um canal de comunicacao
    channel = grpc.insecure_channel("localhost:7000")

    # Inicializacao do stub
    stub = faculdade_pb2_grpc.FaculdadeStub(channel)

    mainWindow(stub)
