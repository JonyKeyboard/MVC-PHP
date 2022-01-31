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
    comando_SQL = "INSERT INTO recibos (nome,preco,descricao) VALUES (%s,%s,%s)"
    dados = (str(nome),str(preco),str(descricao))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEditNome.setText("")
    formulario.doubleSpinBox.clear()
    formulario.lineEdidDesc.setText("")

def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT nome, preco, descricao FROM recibos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(3)
   
    for i in range(0, len(dados_lidos)):
       for j in range(0, 3):
           segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar_dados.ui")
formulario.ButtonGerar.clicked.connect(funcao_principal)
formulario.ButtonGerados.clicked.connect(chama_segunda_tela)

formulario.show()
app.exec()