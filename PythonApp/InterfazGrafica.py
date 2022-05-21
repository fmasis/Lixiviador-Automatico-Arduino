# Interfaz Gráfica Lixiviador
# Desarrollado por: André Arias Ovares
# Tecnológico de Costa Rica

# Impotacion de librerias
import tkinter as tk
import tkinter.font as tkFont
import serial
import time
from tkinter import *

# Configuración ventana principal
raiz = tk.Tk()
raiz.title("Aplicación")
raiz.resizable(False, False)

# Definición de variables
Nombre = tk.StringVar()
INT = tk.IntVar()
INT.set(0)

# Variables que almacenan los tiempos de los intervalos
T1 = tk.IntVar()
T2 = tk.IntVar()
T3 = tk.IntVar()
T4 = tk.IntVar()
T5 = tk.IntVar()
T6 = tk.IntVar()
T7 = tk.IntVar()
T8 = tk.IntVar()
T9 = tk.IntVar()
T10 = tk.IntVar()
T = [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10]

# Variables que almacenan la cantidad de recipientes de cada intervalo
C1 = tk.IntVar()
C2 = tk.IntVar()
C3 = tk.IntVar()
C4 = tk.IntVar()
C5 = tk.IntVar()
C6 = tk.IntVar()
C7 = tk.IntVar()
C8 = tk.IntVar()
C9 = tk.IntVar()
C10 = tk.IntVar()
C = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10]

# Estilos fuentes
fontStyle1 = tkFont.Font(family="Cambria", size=13)
fontStyle2 = tkFont.Font(family="Cambria", size=11)
fontStyle3 = tkFont.Font(family="Cambria", size=26)
fontStyle4 = tkFont.Font(family="Cambria", size=80)
fontStyle5 = tkFont.Font(family="Cambria", size=20)

# Puerto a utilizar
puertoact = "COM1"
puerto = tk.StringVar()
puerto.set(puertoact)

# Comunicacion del arduino
arduino = 0


# Creación de widgets de la ventana principal
def VentanaPrincipal():
    global puertoact
    x1 = 65
    yv = 215
    grid()

    for i in range(0, int(INT.get())):
        tk.Label(raiz, text="Tiempo de Intervalo " + str(i + 1) + ":", font=fontStyle1).place(x=x1, y=yv)
        tk.Entry(raiz, textvariable=T[i], width=10, font=fontStyle1).place(x=x1+170, y=yv)
        tk.Label(raiz, text="# de Recipientes:", font=fontStyle1).place(x=x1+285, y=yv)
        tk.Entry(raiz, textvariable=C[i], width=7, font=fontStyle1).place(x=x1+415, y=yv)
        yv += 60

    tk.Label(raiz, text="Lixiviador", font=fontStyle3).place(x=240, y=25)
    tk.Label(raiz, text="Nombre:", font=fontStyle1).place(x=65, y=95)
    tk.Entry(raiz, textvariable=Nombre, width=37, font=fontStyle1).place(x=137, y=95)
    tk.Button(raiz, text="Cargar", bg="light blue", font=fontStyle2).place(x=488, y=91)
    tk.Label(raiz, text="Cantidad de Intervalos de Tiempo:", font=fontStyle1).place(x=65, y=155)
    tk.Entry(raiz, textvariable=INT, width=17, font=fontStyle1).place(x=318, y=155)
    tk.Button(raiz, text="Aceptar", bg="light blue", font=fontStyle2, command=VentanaPrincipal).place(x=485, y=151)
    tk.Label(raiz, text=("Puerto actual: " + puertoact), font=fontStyle2).place(x=0, y=yv+28)

    # Se agregan los widgets faltantes
    tk.Button(raiz, text="Guardar", bg="light blue", font=fontStyle2).place(x=170, y=yv)
    tk.Button(raiz, text="Iniciar", bg="light blue", font=fontStyle2, command=iniciar).place(x=400, y=yv)

    # Menu desplegable
    menubar = tk.Menu(raiz)
    listamenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Opciones', menu=listamenu)
    listamenu.add_command(label='Seleccionar puerto', command=SeleccionarPuerto)
    raiz.config(menu=menubar)
    raiz.geometry("640x" + str(yv + 70) + "+590+200")


# Elimina el frame actual
def grid():
    for widget in raiz.winfo_children():
        widget.destroy()


# Selecciona del puerto del arduino
def SeleccionarPuerto():
    vPuerto = Toplevel(raiz)
    vPuerto.title("Seleccionar puerto")
    vPuerto.geometry("260x100+770+300")
    tk.Label(vPuerto, text="Introduzca el puerto:").pack()
    tk.Entry(vPuerto, textvariable=puerto, width=20, font=fontStyle1).pack()
    tk.Button(vPuerto, text="Aceptar", bg="light blue", font=fontStyle2,
              command=lambda: [ActualizarPuerto(True), vPuerto.destroy(), VentanaPrincipal()]).place(x=45, y=55)
    tk.Button(vPuerto, text="Cancelar", bg="light blue", font=fontStyle2,
              command=lambda: [ActualizarPuerto(False), vPuerto.destroy()]).place(x=150, y=55)


# Actualiza el valor del puerto actual
def ActualizarPuerto(tipo):
    global puertoact
    if tipo:
        puertoact = puerto.get()
    else:
        puerto.set(puertoact)
    print(puertoact)


# Calculo de los arreglos de minutos y segundos para el temporizador
def Temporizador():
    # Listas para los valores del temporizador
    Aminutos = []
    Asegundos = []
    Arecipientes = []
    Aintervalos = []
    intervalos = 0

    # Interfaz gráfica Temporizador
    vTemporizador = Toplevel(raiz)
    vTemporizador.title("Temporizador")
    vTemporizador.geometry("620x250+770+300")
    tk.Label(vTemporizador, text='Recipientes', font=fontStyle5).place(x=50, y=10)
    tk.Label(vTemporizador, text='faltantes', font=fontStyle5).place(x=65, y=45)
    tk.Label(vTemporizador, text='Tiempo', font=fontStyle5).place(x=386, y=10)
    tk.Label(vTemporizador, text='restante', font=fontStyle5).place(x=384, y=45)
    tk.Button(vTemporizador, text="Cerrar", bg="light blue", font=fontStyle2,
              command=vTemporizador.destroy).place(x=540, y=206)
    Tempo = tk.Label(vTemporizador, text='', font=fontStyle4, fg="green")
    Cant = tk.Label(vTemporizador, text='', font=fontStyle4, fg="green")
    Inter = tk.Label(vTemporizador, text='Intervalo: ' + str(1) + '/' + str(INT.get()), font=fontStyle1, fg="gray")
    Tempo.place(x=300, y=75)
    Cant.place(x=58, y=75)
    Inter.place(x=8, y=222)

    # Generacion de arreglos
    for i in range(0, INT.get()):
        segundos = 0
        recipientes = C[i].get()
        minutos = T[i].get()
        intervalos += 1

        Aminutos.append(minutos)
        Asegundos.append(segundos)
        Arecipientes.append(recipientes)
        Aintervalos.append(intervalos)

        while recipientes != 0:
            if minutos != 0:
                if segundos == 0:
                    minutos = minutos - 1
                    segundos = 59
                else:
                    segundos = segundos - 1
            else:
                if segundos == 0:
                    if recipientes > 1:
                        recipientes = recipientes - 1
                        minutos = T[i].get()
                    elif recipientes == 1:
                        recipientes -= 1
                    else:
                        break
                else:
                    segundos -= 1
            Aminutos.append(minutos)
            Asegundos.append(segundos)
            Arecipientes.append(recipientes)
            Aintervalos.append(intervalos)

    # Adecuacion de los arreglos generados
    Aminutos.pop()
    Asegundos.pop()
    Arecipientes.pop()
    Aminutos.append(0)
    Asegundos.append(0)
    Arecipientes.append(0)

    # Inicio del conteo
    InicioTemporizador(Tempo, Cant, Inter, Aminutos, Asegundos, Arecipientes, Aintervalos, 0, len(Aminutos)-1)


# Temporizador en pantalla
def InicioTemporizador(Tempo, Cant, Inter, minutos, segundos, recipientes, intervalos, i, f):
    global arduino

    # Se cambia el formato de los arreglos de los minutos, segundos y recipientes para mostrarlos en pantalla
    minuto_string = f'{minutos[i]}' if minutos[i] > 9 else f'0{minutos[i]}'
    segundo_string = f'{segundos[i]}' if segundos[i] > 9 else f'0{segundos[i]}'
    recipientes_string = f'{recipientes[i]}' if recipientes[i] > 9 else f'0{recipientes[i]}'

    # Se cambia el valor mostrado en pantalla
    Tempo.config(text=minuto_string + ':' + segundo_string)
    Cant.config(text=recipientes_string)
    Inter.config(text='Intervalo: ' + str(intervalos[i]) + '/' + str(INT.get()))

    # Actualización de los valores del temporizador
    # Cuando se hayan mostrados todos los valores en pantalla se cierra la comunicación
    if i == f:
        print('Cerrando comunicacion...')
        arduino.close()
        print('Comunicación cerrada con éxito')
        return 0
    else:
        # Si el elemento analizado no es el primero del arreglo
        if i != 0:
            # Cuando el contador de minutos y segundos llegue a cero espera una señal del arduino para continuar
            if minutos[i-1] == 0 and segundos[i-1] == 0 and recipientes[i-1]:
                r = int(arduino.readline().decode())
                if r == 9:
                    i += 1
                    Tempo.after(1000, InicioTemporizador, Tempo, Cant, Inter,
                                minutos, segundos, recipientes, intervalos, i, f)
                else:
                    print("Error al recibir el dato del arduino")
            else:
                i += 1
                Tempo.after(1000, InicioTemporizador, Tempo, Cant, Inter,
                            minutos, segundos, recipientes, intervalos, i, f)
        else:
            # Espera una señal del arduino para iniciar el temporizador de la primera muestra
            r = int(arduino.readline().decode())
            print(r)
            if r == 9:
                i += 1
                Tempo.after(1000, InicioTemporizador, Tempo, Cant, Inter,
                            minutos, segundos, recipientes, intervalos, i, f)
            else:
                print("Error arduino")


# Envío de datos al arduino
def iniciar():
    global arduino
    if INT.get() == 0:
        print("Ingrese una cantidad de intervalos mayor a 0.")
    else:
        try:
            print('Abriendo comunicación...')
            arduino = serial.Serial(puertoact, 9600)
            time.sleep(3)
            print("Enviando cantidad de intervalos: " + str(INT.get()))
            arduino.write(str(INT.get()).encode())
            print("Recibiendo cantidad de intervalos: " + arduino.readline().decode())
            print("-----------------------")
            for i in range(0, INT.get()):
                print("Conjunto " + str(i+1))
                print("Enviando tiempo: " + str(T[i].get()))
                arduino.write(str(T[i].get()).encode())
                print("Recibiendo tiempo: " + arduino.readline().decode().rstrip('\n'))
                print("Enviando cantidad de envases: " + str(C[i].get()))
                arduino.write(str(C[i].get()).encode())
                print("Recibiendo cantidad de envases: " + arduino.readline().decode().rstrip('\n') + "\n")
            print("--------------------------")
            Temporizador()
        except serial.serialutil.SerialException:
            print("El puerto seleccionaddo es el incorrecto.")


# Ejecucion de la raiz
VentanaPrincipal()
raiz.mainloop()
