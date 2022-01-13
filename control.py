from sqlite3 import Cursor
from PyQt5 import uic, QtWidgets
import mysql.connector
from datetime import date


banco_cad_cli = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Juni2311@",
    database="app_test"
)


def func_princ():
    nome = formulario.name.text()
    data_nasc = formulario.date_nasc.text()
    cpf = formulario.cpf.text()
    email = formulario.email.text()
    sexo = formulario.sex.text()
    logradouro = formulario.logra.text()
    num_casa = formulario.num_house.text()
    compl = formulario.compl.text()
    cep = formulario.zip_code.text()
    ddd_tele = formulario.ddd_tele.text()
    tele = formulario.tele.text()
    ddd_tele_com = formulario.ddd_tele_com.text()
    tele_com = formulario.tele_com.text()
    
    
    cursor = banco_cad_cli.cursor()
    comand_SQL = "INSERT INTO clientes (nome, data_nasc, cpf, email, sexo, logradouro, numero, compl, cep, tel, tele_com) VALUES(%s, '$date', %s, %s, %s, %s, %d, %s, %s, %s, %s)"
    dados = (str(nome), date(data_nasc), str(cpf), str(email), str(sexo), str(logradouro), int(num_casa), str(compl), str(cep), int(ddd_tele), str(tele), int(ddd_tele_com), str(tele_com))
    cursor.execute(comand_SQL, dados)
    banco_cad_cli.commit()


app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
formulario.send.clicked.connect(func_princ)


formulario.show()
app.exec()