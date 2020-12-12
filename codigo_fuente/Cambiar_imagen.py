# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cambiar_imagen.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Dialog(object):
    def setupUi(self, Dialog):
        '''Esta funcion permite construir y gestionar la interfaz del usuario
        :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria  
        :param objeto Dialog: permite modificar los atributos de la ventana        '''
    
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 195)
        self.Cbox_CambiarImagen = QtWidgets.QComboBox(Dialog)
        self.Cbox_CambiarImagen.setGeometry(QtCore.QRect(20, 30, 171, 22))
        self.Cbox_CambiarImagen.setObjectName("Cbox_CambiarImagen")
        self.Cbox_CambiarImagen.addItem("")
        self.Cbox_CambiarImagen.addItem("")
        self.Cbox_CambiarImagen.addItem("")
        self.Cbox_CambiarImagen.addItem("")
        self.Cbox_CambiarImagen.addItem("")
        self.Cbox_CambiarImagen.addItem("")
        self.Cbox_CambiarImagen.addItem("")
        self.Cbox_CambiarImagen.addItem("")
        self.Cbox_CambiarImagen.addItem("")
        self.Cbox_CambiarImagen.addItem("")
        self.Cbox_CambiarImagen.addItem("")
        self.Cbox_CambiarImagen.addItem("")
        self.Cbox_CambiarImagen.addItem("")
        self.ln_url = QtWidgets.QLineEdit(Dialog)
        self.ln_url.setGeometry(QtCore.QRect(150, 90, 191, 21))
        self.ln_url.setObjectName("ln_url")
        self.Btn_confirmar_url = QtWidgets.QPushButton(Dialog)
        self.Btn_confirmar_url.setGeometry(QtCore.QRect(170, 150, 75, 23))
        self.Btn_confirmar_url.setObjectName("Btn_confirmar_url")
        self.Lbl_ingrese_url = QtWidgets.QLabel(Dialog)
        self.Lbl_ingrese_url.setGeometry(QtCore.QRect(20, 90, 121, 20))
        self.Lbl_ingrese_url.setObjectName("Lbl_ingrese_url")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        '''Permite modificar los atributos de la ventana del usuario
         :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria
         :param objeto Dialog: permite la gestion de la interfaz del usuario
        '''
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cambiar Imagen"))
        self.Cbox_CambiarImagen.setItemText(0, _translate("Dialog", "Seleccione un mes..."))
        self.Cbox_CambiarImagen.setItemText(1, _translate("Dialog", "Enero"))
        self.Cbox_CambiarImagen.setItemText(2, _translate("Dialog", "Febrero"))
        self.Cbox_CambiarImagen.setItemText(3, _translate("Dialog", "Marzo"))
        self.Cbox_CambiarImagen.setItemText(4, _translate("Dialog", "Abril"))
        self.Cbox_CambiarImagen.setItemText(5, _translate("Dialog", "Mayo"))
        self.Cbox_CambiarImagen.setItemText(6, _translate("Dialog", "Junio"))
        self.Cbox_CambiarImagen.setItemText(7, _translate("Dialog", "Julio"))
        self.Cbox_CambiarImagen.setItemText(8, _translate("Dialog", "Agosto"))
        self.Cbox_CambiarImagen.setItemText(9, _translate("Dialog", "Septiembre"))
        self.Cbox_CambiarImagen.setItemText(10, _translate("Dialog", "Octubre"))
        self.Cbox_CambiarImagen.setItemText(11, _translate("Dialog", "Noviembre"))
        self.Cbox_CambiarImagen.setItemText(12, _translate("Dialog", "Diciembre"))
        self.Btn_confirmar_url.setText(_translate("Dialog", "Confirmar"))
        self.Lbl_ingrese_url.setText(_translate("Dialog", "Ingrese Url de la imagen"))
        self.pushButton.setText(_translate("Dialog", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
