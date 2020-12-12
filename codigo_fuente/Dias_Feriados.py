# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dias Feriados.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Festivos_Window(object):
    def setupUi(self, Festivos_Window):
        '''En esta funcion se encuentra la contruccion de la interfaz con la que el usuario podra interactuar
        :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria
        :param Objeto Festivos_Window: Permite contruir la ventana   
        '''
        Festivos_Window.setObjectName("Festivos_Window")
        Festivos_Window.resize(541, 257)
        self.centralwidget = QtWidgets.QWidget(Festivos_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.Cbox_Meses = QtWidgets.QComboBox(self.centralwidget)
        self.Cbox_Meses.setGeometry(QtCore.QRect(30, 20, 231, 22))
        self.Cbox_Meses.setObjectName("Cbox_Meses")
        self.Cbox_Meses.addItem("")
        self.Cbox_Meses.addItem("")
        self.Cbox_Meses.addItem("")
        self.Cbox_Meses.addItem("")
        self.Cbox_Meses.addItem("")
        self.Cbox_Meses.addItem("")
        self.Cbox_Meses.addItem("")
        self.Cbox_Meses.addItem("")
        self.Cbox_Meses.addItem("")
        self.Cbox_Meses.addItem("")
        self.Cbox_Meses.addItem("")
        self.Cbox_Meses.addItem("")
        self.Cbox_Meses.addItem("")
        self.lbl_Fecha = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Fecha.setGeometry(QtCore.QRect(30, 60, 481, 81))
        self.lbl_Fecha.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.lbl_Fecha.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_Fecha.setObjectName("lbl_Fecha")
        self.lbl_Imagen = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Imagen.setGeometry(QtCore.QRect(100, 120, 311, 121))
        self.lbl_Imagen.setText("")
        self.lbl_Imagen.setObjectName("lbl_Imagen")
        self.btn_Aceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Aceptar.setGeometry(QtCore.QRect(280, 20, 75, 23))
        self.btn_Aceptar.setObjectName("btn_Aceptar")
        self.Btn_Opciones = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_Opciones.setGeometry(QtCore.QRect(370, 20, 75, 23))
        self.Btn_Opciones.setObjectName("Btn_Opciones")
        Festivos_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Festivos_Window)
        QtCore.QMetaObject.connectSlotsByName(Festivos_Window)

    def retranslateUi(self, Festivos_Window):
        ''' Permite cambiar y gestionar la interfaz del usuario
        :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria
        :param Objeto Festivos_Window: Permite contruir la ventana '''
        _translate = QtCore.QCoreApplication.translate
        Festivos_Window.setWindowTitle(_translate("Festivos_Window", "Festividades"))
        self.Cbox_Meses.setItemText(0, _translate("Festivos_Window", "Seleccione mes"))
        self.Cbox_Meses.setItemText(1, _translate("Festivos_Window", "Enero"))
        self.Cbox_Meses.setItemText(2, _translate("Festivos_Window", "Febrero"))
        self.Cbox_Meses.setItemText(3, _translate("Festivos_Window", "Marzo"))
        self.Cbox_Meses.setItemText(4, _translate("Festivos_Window", "Abril"))
        self.Cbox_Meses.setItemText(5, _translate("Festivos_Window", "Mayo"))
        self.Cbox_Meses.setItemText(6, _translate("Festivos_Window", "Junio"))
        self.Cbox_Meses.setItemText(7, _translate("Festivos_Window", "Julio"))
        self.Cbox_Meses.setItemText(8, _translate("Festivos_Window", "Agosto"))
        self.Cbox_Meses.setItemText(9, _translate("Festivos_Window", "Septiembre"))
        self.Cbox_Meses.setItemText(10, _translate("Festivos_Window", "Octubre"))
        self.Cbox_Meses.setItemText(11, _translate("Festivos_Window", "Noviembre"))
        self.Cbox_Meses.setItemText(12, _translate("Festivos_Window", "Diciembre"))
        self.lbl_Fecha.setText(_translate("Festivos_Window", "23 de marzo     Día de San José. (Se celebra inicialmente el 19 del mes, pero se traslada al lunes 23)"))
        self.btn_Aceptar.setText(_translate("Festivos_Window", "Aceptar"))
        self.Btn_Opciones.setText(_translate("Festivos_Window", "Opciones"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Festivos_Window = QtWidgets.QMainWindow()
    ui = Ui_Festivos_Window()
    ui.setupUi(Festivos_Window)
    Festivos_Window.show()
    sys.exit(app.exec_())
