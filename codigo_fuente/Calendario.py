# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calendario.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


class Dialog(object):
    def setupUi(self, Dialog):
        self.dia = datetime.now().day
        Dialog.setObjectName("Dialog")
        Dialog.resize(663, 365)
        self.Cal_Fecha = QtWidgets.QCalendarWidget(Dialog)
        self.Cal_Fecha.setGeometry(QtCore.QRect(0, 0, 391, 241))
        self.Cal_Fecha.setStyleSheet("QCalendarWidget QToolButton {\n"
"height: 35px;\n"
"width: 150px;\n"
"font-size: 25px;\n"
"icon-size:35px,35px;\n"
"color:black;\n"
"    selection-background-color: rgb(0, 0, 0);\n"
"}\n"
"QCalendarWidget QWidget{\n"
"font: 75 11pt \"Perpetua Titling MT\";\n"
"alternate-background-color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"\n"
"    selection-color: rgb(0, 0, 255);\n"
"}")
        self.Cal_Fecha.setMinimumDate(QtCore.QDate(2020, 12, self.dia ))
        self.Cal_Fecha.setGridVisible(True)
        self.Cal_Fecha.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.Cal_Fecha.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.Cal_Fecha.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.Cal_Fecha.setNavigationBarVisible(True)
        self.Cal_Fecha.setDateEditEnabled(True)
        self.Cal_Fecha.setObjectName("Cal_Fecha")
        self.btn_Confirmar = QtWidgets.QPushButton(Dialog)
        self.btn_Confirmar.setGeometry(QtCore.QRect(200, 280, 75, 23))
        self.btn_Confirmar.setStyleSheet("font: 75 8pt \"Perpetua Titling MT\";")
        self.btn_Confirmar.setObjectName("btn_Confirmar")
        self.Btn_Festividades = QtWidgets.QPushButton(Dialog)
        self.Btn_Festividades.setGeometry(QtCore.QRect(280, 280, 81, 23))
        self.Btn_Festividades.setStyleSheet("font: 75 8pt \"Perpetua Titling MT\";")
        self.Btn_Festividades.setObjectName("Btn_Festividades")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 250, 181, 31))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.lbl_Seleccione_mes = QtWidgets.QLabel(Dialog)
        self.lbl_Seleccione_mes.setGeometry(QtCore.QRect(420, 60, 141, 31))
        self.lbl_Seleccione_mes.setObjectName("lbl_Seleccione_mes")
        self.lbl_Nombre_usuario = QtWidgets.QLabel(Dialog)
        self.lbl_Nombre_usuario.setGeometry(QtCore.QRect(420, 20, 131, 31))
        self.lbl_Nombre_usuario.setObjectName("lbl_Nombre_usuario")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(420, 110, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(400, 0, 281, 331))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(390, -10, 16, 341))
        self.label_7.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.Txt_eventos = QtWidgets.QPlainTextEdit(Dialog)
        self.Txt_eventos.setGeometry(QtCore.QRect(410, 140, 241, 181))
        self.Txt_eventos.setReadOnly(True)
        self.Txt_eventos.setObjectName("Txt_eventos")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(240, 310, 121, 22))
        self.dateEdit.setStyleSheet("QCalendarWidget QWidget{\n"
"font: 75 8pt \"Perpetua Titling MT\";\n"
"\n"
"}")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(2020, 12, 11))
        self.dateEdit.setObjectName("dateEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 310, 111, 111))
        self.label_2.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-color: rgb(255, 255, 255);\n"
"border:None")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_7.raise_()
        self.label_6.raise_()
        self.Cal_Fecha.raise_()
        self.btn_Confirmar.raise_()
        self.Btn_Festividades.raise_()
        self.label.raise_()
        self.lbl_Seleccione_mes.raise_()
        self.lbl_Nombre_usuario.raise_()
        self.label_5.raise_()
        self.Txt_eventos.raise_()
        self.dateEdit.raise_()
        self.label_2.raise_()

        self.retranslateUi(Dialog)
        self.btn_Confirmar.clicked.connect(self.Cal_Fecha.showSelectedDate)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calendario"))
        self.btn_Confirmar.setText(_translate("Dialog", "Confirmar"))
        self.Btn_Festividades.setText(_translate("Dialog", "Festivos"))
        self.label.setText(_translate("Dialog", "Seleccione una fecha..."))
        self.lbl_Seleccione_mes.setText(_translate("Dialog", "Mes : Selecione una fecha..."))
        self.lbl_Nombre_usuario.setText(_translate("Dialog", "Usuario:"))
        self.label_5.setText(_translate("Dialog", "EVENTOS"))
        self.Txt_eventos.setPlainText(_translate("Dialog", "Selecione un mes..."))
        self.dateEdit.setDisplayFormat(_translate("Dialog", "DD/MM/yyyy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
