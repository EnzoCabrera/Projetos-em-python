import random
import PySimpleGUI as sg


class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            "Com certeza, você deve fazer isso",
            "Não sei, você que sabe",
            "Não faz isso não!",
            "Acho que tá na hora certa!"
        ]

    def Iniciar(self):

        layout = [
            [sg.Text("Faça sua pergunta:")],
            [sg.input()],
            [sg.Output(size=(20, 10))],
            [sg.Button("Decida por mim")]
        ]

        self.janela = sg.Windoww("Decida por mim!", layout=layout)
        while True
            self.eventos, self.valores = self.janela.Read()
            if self.eventos == "Decida por mim":
                print(random.choice(self.respostas))
              


decida = DecidaPorMim()
decida.Iniciar()
