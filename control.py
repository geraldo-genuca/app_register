from PyQt5 import uic, QtWidgets
import mysql.connector


banco_app_cad = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Juni2311@",
    database="app_test"
)


def func_princ():
    nome = formulario.name.text()
    data_nasc = formulario.data_nasc.text()
    cpf = formulario.cpf.text()
    email = formulario.email.text()
    sexo = formulario.sex.text()
    logradouro = formulario.logra.text()
    numero = formulario.num_house.text()
    compl = formulario.compl.text()
    cep = formulario.zip_code.text()
    cep_dig = formulario.zip_code.text()
    ddd_tele = formulario.ddd_tele.text()
    tele = formulario.tele.text()
    ddd_tele_com = formulario.ddd_tele_com.text()
    tele_com = formulario.tele_com.text()
    
    
    cursor = banco_app_cad.cursor()
    comand_SQL = "INSERT INTO cad_pes_fis (nome, data_nasc, cpf, email, sexo, logradouro, +\
                    numero, compl, cep, cep_dig, ddd_tele, tele, ddd_tele_com, tele_com) +\
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    dados = (str(nome), str(data_nasc), str(cpf), str(email), str(sexo), str(logradouro),
                str(numero), str(compl), str(cep), str(cep_dig), str(ddd_tele), str(tele), 
                str(ddd_tele_com), str(tele_com))
    cursor.execute(comand_SQL, dados)
    banco_app_cad.commit()


app = QtWidgets.QApplication([])
formulario = uic.loadUi("form.ui")
formulario.send.clicked.connect(func_princ)


formulario.show()
app.exec()