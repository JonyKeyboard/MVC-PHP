from PyQt5 import  uic,QtWidgets

def funcao_principal():
    nome = formulario.lineEditNome.text()
    valor = formulario.doubleSpinBox.text()
    descricao = formulario.lineEdidDesc.text()

    print("Nome:",nome)
    print("Valor:",valor)
    print("Descrição:",descricao)
    

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.ButtonGerar.clicked.connect(funcao_principal)

formulario.show()
app.exec()