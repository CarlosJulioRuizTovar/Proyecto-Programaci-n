import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from Calendario import Dialog
from web_Scrapping import Web_Scrapping
from Agendar_evento import AgendarE
from login import*
import subprocess


global usuario_de_salida
verificacion, usuario_de_salida = login1.login(login1)

numeroEvento=0

if verificacion == True:
    
 class appCalendario(QDialog):
     
    print(verificacion,' ',usuario_de_salida)

    def __init__(self):
        '''Descripcion: '''
        super().__init__()
        self.ui = Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_Confirmar.clicked.connect(self.aceptar)
        self.ui.Btn_Festividades.clicked.connect(self.festivos)
        self.ui.Cal_Fecha.selectionChanged.connect(self.MostrarFecha)
        self.ui.lbl_Nombre_usuario.setText('Usuario: {}'.format(usuario_de_salida))
        self.ui.Cal_Fecha.selectionChanged.connect(self.mes)
        self.ui.Cal_Fecha.selectionChanged.connect(self.anexarEventos)
        
    
    def anexarEventos(self):
        self.ui.Txt_eventos.clear()
        self.entro = False
        fecha = self.ui.Cal_Fecha.selectedDate()
        N_mes = str(fecha.toPyDate()).split('-')[1]
        print('Nmes: ',N_mes)
        with open ('usuarios/recordatorio.txt','r') as f:
            for line in f:
                try:    
                    if line.startswith(usuario_de_salida):
                      print('linea antes del if : ',line)
                      if N_mes == line.split(';')[3].split(':')[1].split('-')[1]:
                        
                        print(line)
                        print(type(line))
                        fecha = line.split(';')[3].split(':')[1]
                        hora = line.split(';')[4][5:]
                        titulo = line.split(';')[1].split(':')[1]
                        print(fecha,hora,titulo)
                        self.entro = True
                        self.concatenarEventos(Fecha=fecha, Hora=hora, Titulo=titulo,)
                      elif self.entro == False:
                        self.ui.Txt_eventos.clear()
                        self.ui.Txt_eventos.insertPlainText('No hay Eventos en este mes para este usuario')
                    elif self.entro == False:
                        self.ui.Txt_eventos.clear()
                        #self.ui.Txt_eventos.insertPlainText('No hay Eventos para este usuario')
                except:
                    self.ui.Txt_eventos.clear()
                    self.ui.Txt_eventos.insertPlainText('No hay Eventos para este usuario')
                

    def concatenarEventos(self,**kwargs):
        i = 0
        Cadena = ''
        for key,value in kwargs.items():
            if i == 0:
                Cadena += ''
            else:
                Cadena += '\n'
            Cadena += '{} : {}'.format(key,value)
            i += 1
        
        self.ui.Txt_eventos.insertPlainText('{} \n\n'.format(Cadena))
        




    def mes(self):
        fecha = self.ui.Cal_Fecha.selectedDate()
        N_mes = str(fecha.toPyDate()).split('-')[1]
        lista_meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        self.ui.lbl_Seleccione_mes.setText('Eventos de {} '.format(lista_meses[int(N_mes)-1]))

    def MostrarFecha(self):
        fecha = self.ui.Cal_Fecha.selectedDate()
        fecha_cadena = str(fecha.toPyDate())
        self.ui.label.setText('La fecha es: {}'.format(fecha_cadena))

    def aceptar(self):
        fecha = self.ui.Cal_Fecha.selectedDate()
        fecha_cadena=str(fecha.toPyDate())
        
        self.VentanaExtra = AgendarEvento(fecha_cadena)
        self.VentanaExtra.show()

    def festivos(self):
        self.otraVentana = Web_Scrapping()
        self.otraVentana.show()
    
 class AgendarEvento(QDialog):

    def __init__(self,fecha_cadena):
        super().__init__()
        self.fecha_cadena=fecha_cadena
        self.ui = AgendarE()
        self.ui.setupUi(self)
        self.show()
        print(self.fecha_cadena)
        self.ui.Btn_confirmar.clicked.connect(self.guardarTxt)
        self.ui.Btn_confirmar.clicked.connect(self.fijarAlarma)
        
        
    def guardarTxt(self):
        print(self.fecha_cadena)
        self.hora = (self.ui.Tiempo_usuario.time())
        self.hora = self.hora.toString('HH:mm')
        self.titulo = self.ui.ln_Evento.text()
        self.descripcion = self.ui.Txt_Descripcion.toPlainText()
        
        f = open('usuarios/Recordatorio.txt','a')
        f.write('{} :;Titulo:{};Descripcion:{};Fecha:{};Hora:{}; \n'.format(usuario_de_salida,self.titulo,self.descripcion,self.fecha_cadena,self.hora))
        f.close()

    def fijarAlarma(self):
        dia = self.fecha_cadena.split('-')[2]
        hora = self.hora
        mes = self.fecha_cadena.split('-')[1]
        print(dia ,': ',hora,' ',mes)
        meses = ['JUN','FEB','MAR','APR','MAY','JUNE','JUL','AUG','SEP','OCT','NOV','DEC']
        numeroEventoS = str(numeroEvento)
        carpeta = "Alarma/Alarma"+numeroEventoS+".bat"

        if self.ui.Check_Diario.isChecked() == True:
            with open(carpeta,'wb') as f:
                f.write('schtasks /create /tn Recordatorio /tr D:\python_calendario\Alarma\Alarma{}.vbs /sc monthly /d {} /m {} /st {} /f \n'.format(numeroEvento,dia,meses[int(mes)-1],hora).encode())
            self.mostrarAlarma()
            print('Dias')

        elif self.ui.check_Mes.isChecked() == True:
            with open(carpeta,'wb') as f:
                f.write('schtasks /create /tn Recordatorio /tr D:\python_calendario\Alarma\Alarma{}.vbs /sc monthly /d {} /m {} /st {} /f \n'.format(numeroEvento,dia,meses[int(mes)-1],hora).encode())
            self.mostrarAlarma()
            print('Mes')
        else:
            with open(carpeta,'wb') as f:
                f.write('schtasks /create /tn Recordatorio /tr D:\python_calendario\Alarma\Alarma{}.vbs /sc monthly /d {} /m {} /st {} /f \n'.format(numeroEvento,dia,meses[int(mes)-1],hora).encode())
            self.mostrarAlarma()
            print('Ninguna')
            
        print(carpeta)
        file = "Alarma"+numeroEventoS+".bat"
        #print(file)
        #import os
        #os.chdir(file)
        #os.startfile("ask.bat")

        from subprocess import Popen
        p = Popen(file, cwd=r"D:\python_calendario\Alarma")
        stdout, stderr = p.communicate()

    def mostrarAlarma(self):
        numeroEventoS = str(numeroEvento)
        titulo = self.ui.ln_Evento.text() 
        mensaje = self.ui.Txt_Descripcion.toPlainText()          
        
        carpeta = 'Alarma/alarma' + numeroEventoS + '.vbs'
        with open(carpeta, 'wb') as f:
            f.write('CreateObject(\"WScript.Shell\").Popup {}, 12, {}, 0 + 64 '.format(mensaje,titulo).encode())
        
        #CreateObject("WScript.Shell").Popup "MENSAJE", DURACIÓN, "TITULO", TIPO-POP-UP
        self.incrementar()

    def incrementar(self):
        global numeroEvento
        numeroEvento += 1
 
 if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    dialog = appCalendario()
    dialog.show()
    sys.exit(app.exec_())
       

