from sqlite3 import Cursor
from PyQt5 import uic, QtWidgets
import mysql.connector
from datetime import date


banco_app_cad = mysql.connector.connect(
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
    cep_dig = formulario.cep_dig.text()
    ddd_tele = formulario.ddd_tele.text()
    tele = formulario.tele.text()
    ddd_tele_com = formulario.ddd_tele_com.text()
    tele_com = formulario.tele_com.text()
    
    
    cursor = banco_app_cad.cursor()
    comand_SQL = "INSERT INTO clientes (nome, data_nasc, cpf, email, sexo, logradouro, numero, compl, cep, cep_dig, ddd_tel, tel, ddd_tele_com, tele_com) VALUES(%s, '$date', %s, %s, %s, %s, %d, %s, %d, %d, %d, %d, %d, %d)"
    dados = (str(nome), date(data_nasc), str(cpf), str(email), str(sexo), str(logradouro), int(num_casa), str(compl), int(cep), int(cep_dig), int(ddd_tele), int(tele), int(ddd_tele_com), int(tele_com))
    cursor.execute(comand_SQL, dados)
    banco_app_cad.commit()


app = QtWidgets.QApplication([])
formulario = uic.loadUi("form.ui")
formulario.send.clicked.connect(func_princ)


formulario.show()
app.exec()