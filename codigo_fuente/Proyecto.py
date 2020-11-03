import calendar
import tkinter as tk
import datetime

ano = datetime.date.today().year
mes = datetime.date.today().month
#calendar.LocaleTextCalendar(locale='es_ES')

app = tk.Tk()
app.title("Calendario")
app.config(bg="black")

frame = tk.Frame(app, bg='black')
frame2 = tk.Frame(app, bg='black')
frame3 = tk.Frame(app, bg='black')
frame4 = tk.Frame(app, bg='black')
lista_botones = []

def Calendario(ano, mes):
    """
    Permite crear una cadena donde se representa el mes junto con el año y sus días para separar los
    elementos que serán usados para almacenar información ingresada por el usuario.
    :param int ano: es una variable que contiene el año en curso para el sistema
    :param int mes: es una variable que contiene el número del mes en curso para el sistema
    """
    fecha_general = calendar.month(ano, mes)
    lista_a = (fecha_general.split("\n")[:2])
    lista1 = (lista_a[0])
    lista4 = lista1.split()
    lista2 = (lista_a[1])
    lista3 = lista2.split()
    matriz_cal = []

    for i in range(len(lista4)):
        boton1= tk.Button(frame4, text=lista4[0], fg='white', bg="black", font=("", 16, "bold"), bd=0, width=len("september"))
        boton1a = tk.Button(frame4, text=lista4[1], fg='white', bg="black", font=("", 16, "bold"), bd=0)
        if len(lista4[0]) != len('September') :
            boton1.config(width=len('September'))
        if len(lista4[1]) != len("0000"):
            boton1a.config(width=len('0000'))
        boton1.grid(row=1, column=1)
        boton1a.grid(row=1, column=2)
    frame4.grid(row=1, column=1)

    for i in range(len(lista3)):
        boton= tk.Button(frame3, text=lista3[i], fg="white", bg="black", font=("arial", 15, "bold"), bd=0)
        boton.grid(row=1, column=i+1)
        frame3.grid(row=2, column=1)

    for i in fecha_general.split("\n")[2:]:
        matriz_fila = []
        for j in range(0, len(i), 3):
            matriz_fila.append(i[j:j + 2])
        if (len(matriz_fila) > 0):
            matriz_cal.append(matriz_fila)

    for i in lista_botones:
        i.destroy()
    lista_botones.clear()

    for i in range(len(matriz_cal)):
        for j in range(len(matriz_cal[i])):
            a = matriz_cal[i][j]
            def ventana():
                """
                Genera una ventana al oprimir cada día representado por un número.
                :param int None
                """
                window = tk.Toplevel(app)
                entrada = tk.Entry(window, width=15 )
                entrada.grid(column = 1, row = 1)
                label = tk.Label(window, text="Escriba un evento", fg='white', bg='black', font=("", 12, "bold"))
                label.grid(row=1, column=0)
                for i in fecha_general.split("\n")[2:]:
                    i1 = (i.split())
                    window.title(i1)

            if a != "  ":
                boton = tk.Button(frame2, text=matriz_cal[i][j], command=ventana, fg="white", bg="black", font=("", 16, "bold"), bd=0)
                boton.grid(row=i+1, column=j+3)
                lista_botones.append(boton)
                frame2.grid(row=3, column=1)

def mes_anterior():
    """
    Permite ir disminuyendo el nùmero del mes de 1 en 1 con el fin de que el usuario pueda visualizar
    la disposiciòn del mes anterior al que se presenta en pantalla.
    :param None
    """
    global mes, ano
    mes -= 1
    if mes == 0:
        mes = 12
        ano -= 1
    Calendario(ano, mes)

def mes_siguiente():
    """
    Permite ir aumentando el nùmero del mes de 1 en 1 con el fin de que el usuario pueda visualizar
    la disposicion del mes posterior al que se presenta en pantalla.
    :param None
    """
    global mes, ano
    mes += 1
    if mes == 13:
        mes = 1
        ano += 1
    Calendario(ano, mes)

ant = tk.Button(frame, text="Mes Anterior", command=mes_anterior, fg='white', bg='black', font=("arial", 15, "bold"), bd=0)
ant.grid(row=1, column=1)
sig = tk.Button(frame, text="Mes Siguiente", command=mes_siguiente, fg='white', bg='black', font=("arial", 15, "bold"), bd=0)
sig.grid(row=1, column=2)
frame.grid(row=4, column=1)

Calendario(ano, mes)
app.mainloop()