import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from Dias_Feriados import Festivos_Window
import requests
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from Cambiar_imagen import Dialog

class Web_Scrapping(QMainWindow):
    def __init__(self):
        '''
        Construye la clase
        :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria
        
        '''
        print(type(self))
        super().__init__()

        self.ui = Festivos_Window()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_Aceptar.clicked.connect(self.aceptar)
        self.ui.Btn_Opciones.clicked.connect(self.opciones)

    def opciones(self):
        ''' 
        Crea un objeto de la clase OpcionesD y lo muestra por pantalla
        :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria
        '''

        self.opciones=OpcionesD()
        self.opciones.show()

    def aceptar(self):
        ''' Permite mostrar en pantalla los datos segun el mes elegido, haciendo uso del web scrapping para extraer informacion
        de un sitio web
         :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria
           '''

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_flags = ssl.CERT_NONE

        url = 'https://cnnespanol.cnn.com/2020/08/03/dias-feriados-en-colombia-2020-festivos-colombia-lunes-fechas-mes/'
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        lista=list()

        for evento in soup.find_all('p'):
            texto=evento.text
            lista.append(texto)
         
        listareducida=list()    
        for palabra in lista[7:25]:
            listareducida.append(palabra)
            print(palabra)








        mes=self.ui.Cbox_Meses.itemText(self.ui.Cbox_Meses.currentIndex())
        if mes == 'Enero':
            urlI=self.IngresarUrl(mes)
            self.imagenes(urlI,mes)
            eventos='''{}
{}'''.format(listareducida[0],listareducida[1])
            self.Remplazar(eventos)

        elif mes == 'Marzo':
            urlI=self.IngresarUrl(mes)
            self.imagenes(urlI,mes)
            eventos=listareducida[2]
            self.Remplazar(eventos)

        elif mes == 'Abril':
            urlI=self.IngresarUrl(mes)
            self.imagenes(urlI,mes)
            eventos='''{}
{}'''.format(listareducida[3],listareducida[4])
            self.Remplazar(eventos)

        elif mes == 'Mayo':
            urlI=self.IngresarUrl(mes)
            self.imagenes(urlI,mes)
            eventos='''{}
{}'''.format(listareducida[5],listareducida[6])
            self.Remplazar(eventos)

        elif mes == 'Junio':
            urlI=self.IngresarUrl(mes)
            self.imagenes(urlI,mes)
            eventos='''{}
{}
{}'''.format(listareducida[7],listareducida[8],listareducida[9])
            self.Remplazar(eventos)

        elif mes == 'Julio':
            urlI=self.IngresarUrl(mes)
            self.imagenes(urlI,mes)
            eventos=listareducida[10]
            self.Remplazar(eventos)

        elif mes == 'Agosto':
            urlI=self.IngresarUrl(mes)
            self.imagenes(urlI,mes) 
            eventos='''{}
{}'''.format(listareducida[11],listareducida[12])
            self.Remplazar(eventos)
            

        elif mes == 'Octubre' :
            urlI=self.IngresarUrl(mes)
            self.imagenes(urlI,mes)
            self.Remplazar(listareducida[13])

        elif mes=='Noviembre':
            urlI=self.IngresarUrl(mes)
            self.imagenes(urlI,mes)

            eventos='''{}
{}'''.format(listareducida[14],listareducida[15])
            self.Remplazar(eventos)
        elif mes=='Diciembre':
            eventos='''{}
{}'''.format(listareducida[16],listareducida[17])
            #urlI= "https://www.agenciapi.co/sites/default/files/styles/foto_noticia_principal/public/2018-12/Navidad.jpg?h=c673cd1c&itok=-QlN6Qwl"
            urlI=self.IngresarUrl(mes)
            
            self.imagenes(urlI,mes)
            self.Remplazar(eventos)
        else:
            eventos='Este mes no hay Celebraciones importantes...'
            self.Remplazar(eventos)





    def IngresarUrl(self,nombreTxt):
        '''Guarda la informacion en un archivo txt 
         :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria
         :param String nombreTxt: variable que guarda el nombre del archivo para buscar la imagen
          '''
        nombreTxt=nombreTxt+'.txt'
        f=open('imagenes/{}'.format(nombreTxt),'r')
        url=f.read()
        f.close()
        return url


    def Remplazar(self,eventos):
        '''Muestra en el label la informacion obtenida por la pagina web
        :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria 
        :param String eventos: variable que almacena la informacion mostrada en e label
        '''
        self.ui.lbl_Fecha.setText(eventos)

    def imagenes(self,url,nombre_Imagen):
        '''Guarda el url obtenido de la imagen y lo almacena en un txt
        :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria
        :param String url: variable que almacena el url de la imagen
        :param nombre_Imagen: almacena el nombre de la imagen'''
        nombre_Imagen=nombre_Imagen+'.jpg'
        url_imagen = url
        nombre_local_imagen ='imagenes/{}'.format( nombre_Imagen)
        imagen = requests.get(url_imagen).content
        with open(nombre_local_imagen, 'wb') as handler:
	        handler.write(imagen)
        self.ponerImagen(nombre_local_imagen)

    def ponerImagen(self,nombre_local_imagen):
        '''Muestra por pantalla la imagen en un label
        :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria
        :param String nombre_local_imagen: Variable que almacena la ubicacion de la imagen'''
        imagen = QPixmap(nombre_local_imagen)
        self.ui.lbl_Imagen.setPixmap(imagen)
        self.ui.lbl_Imagen.setScaledContents(True)

class OpcionesD(QDialog):
    '''Clase que muestra por pantalla una ventana emergente con las opciones del programa '''
    def __init__(self):
    
        super().__init__()

        self.ui = Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.Btn_confirmar_url.clicked.connect(self.confirmar)

    def confirmar(self):
        '''Permite realizar el cambio de la imagen mediante el url
        :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria
         '''
        
        mes=self.ui.Cbox_CambiarImagen.itemText(self.ui.Cbox_CambiarImagen.currentIndex())
        


        if mes == 'Enero':
            url=self.ui.ln_url.text()
            self.Remplazar(url,mes)

        elif mes == 'Marzo':
            url=self.ui.ln_url.text()
            self.Remplazar(url,mes)

        elif mes == 'Abril':
            url=self.ui.ln_url.text()
            self.Remplazar(url,mes)

        elif mes == 'Mayo':
            url=self.ui.ln_url.text()
            self.Remplazar(url,mes)
        elif mes == 'Junio':
            url=self.ui.ln_url.text()
            self.Remplazar(url,mes)

        elif mes == 'Julio':
            url=self.ui.ln_url.text()
            self.Remplazar(url,mes)
        elif mes == 'Agosto':
            url=self.ui.ln_url.text()
            self.Remplazar(url,mes)
        elif mes == 'Octubre' :
            url=self.ui.ln_url.text()
            self.Remplazar(url,mes)
        elif mes=='Noviembre':
            url=self.ui.ln_url.text()
            self.Remplazar(url,mes)
        elif mes=='Diciembre':
            url=self.ui.ln_url.text()
            self.Remplazar(url,mes)
        
        
    def Remplazar(self,url,mes):
        '''Remplaza el url de la imagen en el archivo .txt
        :param __main__.Web_Scrapping self: hace la funcion de puntero en una variable hacia la memoria
        :param  String url: variable que almacena el url
        :param  String mes: variable que almacena el nombre del mes
        '''
        Nmes= mes+'.txt'
        f=open('imagenes/{}'.format(Nmes),'wb')
        
        
        f.write('{}'.format(url).encode())
        f.close()
        self.close()
















if __name__ == "__main__":
 
    app = QApplication(sys.argv)
    dialog =Web_Scrapping()
    dialog.show()
    sys.exit(app.exec_())
       