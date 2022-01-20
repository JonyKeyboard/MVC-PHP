from PyQt5 import  uic,QtWidgets
import mysql.connector  

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_recibos"
)

def funcao_principal():
    nome = formulario.lineEditNome.text()
    preco = formulario.doubleSpinBox.text().replace(',' , '.')
    descricao = formulario.lineEdidDesc.text()

    print("Nome:",nome)
    print("Preco:",preco)
    print("Descrição:",descricao)
    

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO recibos (descricao,preco,nome) VALUES (%s,%s,%s)"
    dados = (str(descricao),str(preco),str(nome))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEditNome.setText("")
    formulario.doubleSpinBox.clear()
    formulario.lineEdidDesc.setText("")
    
    

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.ButtonGerar.clicked.connect(funcao_principal)

formulario.show()
app.exec()