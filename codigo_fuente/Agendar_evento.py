# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Agendar_evento.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class AgendarE(object):
    def setupUi(self, AgendarE):
        AgendarE.setObjectName("AgendarE")
        AgendarE.resize(385, 296)
        self.Txt_Descripcion = QtWidgets.QPlainTextEdit(AgendarE)
        self.Txt_Descripcion.setGeometry(QtCore.QRect(160, 60, 211, 81))
        self.Txt_Descripcion.setObjectName("Txt_Descripcion")
        self.label = QtWidgets.QLabel(AgendarE)
        self.label.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label.setObjectName("label")
        self.Tiempo_usuario = QtWidgets.QTimeEdit(AgendarE)
        self.Tiempo_usuario.setGeometry(QtCore.QRect(160, 160, 118, 22))
        self.Tiempo_usuario.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.Tiempo_usuario.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.Tiempo_usuario.setObjectName("Tiempo_usuario")
        self.label_2 = QtWidgets.QLabel(AgendarE)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 121, 16))
        self.label_2.setObjectName("label_2")
        self.Btn_confirmar = QtWidgets.QPushButton(AgendarE)
        self.Btn_confirmar.setGeometry(QtCore.QRect(110, 260, 75, 23))
        self.Btn_confirmar.setObjectName("Btn_confirmar")
        self.Btn_cancelar = QtWidgets.QPushButton(AgendarE)
        self.Btn_cancelar.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.Btn_cancelar.setObjectName("Btn_cancelar")
        self.ln_Evento = QtWidgets.QLineEdit(AgendarE)
        self.ln_Evento.setGeometry(QtCore.QRect(160, 20, 211, 20))
        self.ln_Evento.setObjectName("ln_Evento")
        self.label_3 = QtWidgets.QLabel(AgendarE)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 111, 16))
        self.label_3.setObjectName("label_3")
        self.Check_Diario = QtWidgets.QCheckBox(AgendarE)
        self.Check_Diario.setGeometry(QtCore.QRect(40, 190, 81, 21))
        self.Check_Diario.setObjectName("Check_Diario")
        self.dateEdit_Hasta = QtWidgets.QDateEdit(AgendarE)
        self.dateEdit_Hasta.setGeometry(QtCore.QRect(160, 200, 110, 22))
        self.dateEdit_Hasta.setStyleSheet("QCalendarWidget QWidget{\n"
"font: 75 9pt \"Perpetua Titling MT\";\n"
"}")
        self.dateEdit_Hasta.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 12, 14), QtCore.QTime(0, 0, 0)))
        self.dateEdit_Hasta.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 12, 11), QtCore.QTime(0, 0, 0)))
        self.dateEdit_Hasta.setCalendarPopup(True)
        self.dateEdit_Hasta.setObjectName("dateEdit_Hasta")
        self.check_Mes = QtWidgets.QCheckBox(AgendarE)
        self.check_Mes.setGeometry(QtCore.QRect(40, 210, 70, 17))
        self.check_Mes.setObjectName("check_Mes")
        self.label_4 = QtWidgets.QLabel(AgendarE)
        self.label_4.setGeometry(QtCore.QRect(120, 200, 41, 21))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(AgendarE)
        self.Btn_cancelar.clicked.connect(AgendarE.close)
        QtCore.QMetaObject.connectSlotsByName(AgendarE)

    def retranslateUi(self, AgendarE):
        _translate = QtCore.QCoreApplication.translate
        AgendarE.setWindowTitle(_translate("AgendarE", "Agendar Evento"))
        self.label.setText(_translate("AgendarE", "Evento que desea guardar"))
        self.Tiempo_usuario.setDisplayFormat(_translate("AgendarE", "h:mm AP"))
        self.label_2.setText(_translate("AgendarE", "Seleccione la hora"))
        self.Btn_confirmar.setText(_translate("AgendarE", "Confirmar"))
        self.Btn_cancelar.setText(_translate("AgendarE", "Cancelar"))
        self.label_3.setText(_translate("AgendarE", "Descripción"))
        self.Check_Diario.setText(_translate("AgendarE", "Diario"))
        self.check_Mes.setText(_translate("AgendarE", "Mensual"))
        self.label_4.setText(_translate("AgendarE", "hasta:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgendarE = QtWidgets.QDialog()
    ui = Ui_AgendarE()
    ui.setupUi(AgendarE)
    AgendarE.show()
    sys.exit(app.exec_())
