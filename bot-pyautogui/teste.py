from PyQt5 import uic,QtWidgets

def botaoClicado():
    print("Funcionou")


app=QtWidgets.QApplication([])
tela=uic.loadUi("bot-pyautogui/tela.ui")
tela.botao.clicked.connect(botaoClicado)

tela.show()
app.exec()