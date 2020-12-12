import tkinter as tk
import os

global verifica
verifica = False

global usuario_de_salida
usuario_de_salida = "Usuario"

class login1:
    def login(self):
        """
        Crea una ventana en la cual se introducirán los datos de usuario y contraseña
        :param type self: se refiere al objeto que en ese momento está ejecutando el método (a sí mismo)
        """
        global window
        window = tk.Tk()
        window.title('Login')
        window.geometry('250x150')

        window.configure(bg='black')

        entrada1 = tk.Entry(window, width=10)
        entrada2 = tk.Entry(window, width=10)

        label_entrada1 = tk.Label(window, text='Usuario:', font=('Arial bold', 12), bg="black", fg="white")
        label_entrada1.grid(column=0, row=1)
        label_entrada2 = tk.Label(window, text='Contraseña: ', font=('Arial bold', 12), bg="black", fg="white")
        label_entrada2.grid(column=0, row=2)

        entrada1.grid(column=1, row=1)
        entrada2.grid(column=1, row=2)

        boton = tk.Button(window, text="Ingresar", command= lambda: login1.acceder(entrada1.get(), entrada2.get()))
        boton.grid(column=1, row=3)

        boton2 = tk.Button(window, text="Registrar", command= lambda: login1.registrar(entrada1.get(), entrada2.get()))
        boton2.grid(column=1, row=4)

        window.mainloop()
        return verifica, usuario_de_salida

    def registrar(usuario, contrasena):
        """
        Guarda los datos de usuario y contraseña en un diccionario y también en un archivo .txt. Además, si se ingresa el nombre de un usuario ya registrado, imprime un mensaje de error y obliga a la persona a introducir otro nombre de usuario
        :param str usuario: se refiere al nombre de usuario ingresado
        :param str contrasena: se refiere a la contraseña ingresada
        """
        archivo = "usuarios/login.txt"  # "C:/Users/USUARIO/Desktop/login.txt"

        archivo_existente, dic = login1.leerArchivo(login1)

        if usuario in dic:
            str_texto1=tk.StringVar()
            str_texto1.set("")
            str_texto1.set("Usuario inválido")
            label_resultado = tk.Label(window, textvariable=str_texto1, font=('Arial bold', 12), bg="black", fg="red")
            label_resultado.config(text=" ")
            label_resultado.grid(column=0, row=3)
            return

        elif archivo_existente == True:
            # Abre el archivo
            file_object = open(archivo, 'a')
            # Añade el usuario y contraseña al archivo txt (usuario,contraseña;)
            file_object.write(str(usuario) + ',' + str(contrasena) + ';')
            # Cierra el archivo
            file_object.close()
        else:
            print("Registrando archivo de contraseñas")

    def acceder(usuario, contrasena):
        """
        Verifica si el usuario y la contraseña ingresados son correctos, y abre la ventana del calendario en caso de verdadero
        :param str usuario: se refiere al nombre de usuario ingresado
        :param str contrasena: se refiere a la contraseña ingresada
        """
        a, dic = login1.leerArchivo(login1)

        print(dic)

        try:
            global verifica
        except:
            verifica = False

        try:
            if dic[usuario] == contrasena:
                try:
                    global usuario_de_salida
                    usuario_de_salida = usuario
                except:
                    usuario_de_salida = usuario
                
                verifica = True
                window.destroy()
            else:
                verifica = False
                str_texto=tk.StringVar()
                str_texto.set("")
                str_texto.set("        Error          ")
                
                label_resultado = tk.Label(window, textvariable=str_texto, font=('Arial bold', 12), bg="black", fg="red")
                label_resultado.config(text=" ")
                label_resultado.grid(column=0, row=3)
        except:
            str_texto=tk.StringVar()
            str_texto.set("")
            str_texto.set("Error")
            label_resultado = tk.Label(window, textvariable=str_texto, font=('Arial bold', 12), bg="black", fg="red")
            label_resultado.grid(column=0, row=3)

    def leerArchivo(self):
        """

        :param type self: se refiere al objeto que en ese momento está ejecutando el método (a sí mismo)
        """
        archivo = "usuarios/login.txt"#"C:/Users/USUARIO/Desktop/login.txt"
        archivo_existente = os.path.isfile(archivo)
        dic = {}
        if archivo_existente == False:
            print("Registrando archivo de contraseñas")
            login1.crear(archivo)

        with open(archivo, mode="r", encoding=" utf-8") as fileReader:
            texto = fileReader.read()
            usuario1 = texto.split(";")
            for i in usuario1:

                try:
                    if len(i) > 0:
                        datos = i.split(",")
                        dic[datos[0]] = datos[1]
                except:
                    print()

        archivo_existente = os.path.isfile(archivo)

        return archivo_existente, dic

    def crear(archivo):
        """

        :param  archivo:
        """

        archivo1 = open(archivo, "w")
        archivo1.close()