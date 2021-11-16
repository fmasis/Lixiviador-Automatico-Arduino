from tkinter import *
import tkinter
from tkinter import ttk
import serial
import json

arduino = serial.Serial('COM3',9600)
def cargar1():
    xv = 0
    with open('data1.json') as file:
        data = json.load(file)
        for client in data['intervalo']:
            TEL[xv].set(client['Tiempo'])
            TEN[xv].set(client['Cantidad'])
            nombre.set(client['Nombre'])
            xv += 1
            ##print(data)
        CRP.set(xv)
        frame1()
def cargar2():
    xv = 0
    with open('data2.json') as file:
        data = json.load(file)
        for client in data['intervalo']:
            TEL[xv].set(client['Tiempo'])
            TEN[xv].set(client['Cantidad'])
            nombre.set(client['Nombre'])
            xv += 1
            ##print(data)
        CRP.set(xv)
        frame2()
def cargar3():
    xv = 0
    with open('data3.json') as file:
        data = json.load(file)
        for client in data['intervalo']:
            TEL[xv].set(client['Tiempo'])
            TEN[xv].set(client['Cantidad'])
            nombre.set(client['Nombre'])
            xv += 1
            ##print(data)
        CRP.set(xv)
        frame3()
def cargar4():
    xv = 0
    with open('data4.json') as file:
        data = json.load(file)
        for client in data['intervalo']:
            TEL[xv].set(client['Tiempo'])
            TEN[xv].set(client['Cantidad'])
            nombre.set(client['Nombre'])
            xv += 1
            ##print(data)
        CRP.set(xv)
        frame4()

def saludo():
    print("Enviando datos a arduino")
    print(TE.get());
    #arduino.write(TE.get().encode())
def iniciar():
    data = {}
    print("Enviando " + CRP.get())
    arduino.write(CRP.get().encode())
    print("Recibiendo " + arduino.readline().decode())
    xv = 0;
    print("-----------------------")
    while(xv <= int(CRP.get())-1):
        print("Enviando "+ TEL[xv].get())
        arduino.write(TEL[xv].get().encode())
        print("Recibiendo " + arduino.readline().decode().rstrip('\n'))
        print("Enviando " + TEN[xv].get())
        arduino.write(TEN[xv].get().encode())
        print("Recibiendo " + arduino.readline().decode().rstrip('\n'))
        xv += 1
        print(xv)
    print("--------------------------")
    while(True):
        print("Recibiendo " + arduino.readline().decode().rstrip('\n'))

def GuardarConfig1():
    data = {}
    data['intervalo'] = []
    xv = 0
    while(xv <= int(CRP.get()) -1):
        data['intervalo'].append({
            'Tiempo' : TEL[xv].get(),
            'Cantidad' : TEN[xv].get(),
            'Nombre' : nombre.get()})
        xv += 1
    with open('data1.json', 'w') as file:
        json.dump(data,file,indent=4)
    print(data)
def GuardarConfig2():
    data = {}
    data['intervalo'] = []
    xv = 0
    while(xv <= int(CRP.get()) -1):
        data['intervalo'].append({
            'Tiempo' : TEL[xv].get(),
            'Cantidad' : TEN[xv].get(),
            'Nombre' : nombre.get()})
        xv += 1
    with open('data2.json', 'w') as file:
        json.dump(data,file,indent=4)
    print(data)
def GuardarConfig3():
    data = {}
    data['intervalo'] = []
    xv = 0
    while(xv <= int(CRP.get()) -1):
        data['intervalo'].append({
            'Tiempo' : TEL[xv].get(),
            'Cantidad' : TEN[xv].get(),
            'Nombre' : nombre.get()})
        xv += 1
    with open('data3.json', 'w') as file:
        json.dump(data,file,indent=4)
    print(data)
def GuardarConfig4():
    data = {}
    data['intervalo'] = []
    xv = 0
    while(xv <= int(CRP.get()) -1):
        data['intervalo'].append({
            'Tiempo' : TEL[xv].get(),
            'Cantidad' : TEN[xv].get(),
            'Nombre' : nombre.get()})
        xv += 1
    with open('data4.json', 'w') as file:
        json.dump(data,file,indent=4)
    print(data)
    
def grid(frame):
    for widget in P[frame].winfo_children():
        widget.destroy()
        
def frame1():
    frame = 0;
    CrearIntervalos(0)
    
def frame2():
    frame = 1;
    CrearIntervalos(1)
    
def frame3():
    frame = 2;
    CrearIntervalos(2)
    
def frame4():
    frame = 3;
    CrearIntervalos(3)

def CrearIntervalos(frame):
    grid(frame)
    x1 = 20
    x2 = 145
    x3 = 323
    x4 = 423
    yv = 130
    xv = 0
    while(xv <= int(CRP.get()) -1):
        L1 = Label(P[frame],text="Tiempo de Intervalo " + str(xv+1) + ":").place(x = x1, y = yv)
        I1 = Entry(P[frame],textvariable=TEL[xv], width=35).place(x = x2, y = yv)
        LN = Label(P[frame],text="# de Recipientes:").place(x = x3, y = yv)
        IN = Entry(P[frame],textvariable=TEN[xv], width=5).place(x = x4, y = yv)
        #D1 = Checkbutton(P[frame], text="¿Detener?", variable=var1).place(x = x3, y = yv)
        yv += 50
        xv += 1
    Label(P[frame],text="Nombre: ").place(x=20,y=30)
    Entry(P[frame],textvariable=nombre, width=50).place(x=75,y=30)
    Label(P[frame],text="Cantidad de Intervalos de Tiempo:").place(x=20,y=80)
    Entry(P[frame],textvariable=CRP, width=18).place(x=210,y=80)
    if(frame == 0):
        Button(P[frame], text="Aceptar", bg="light blue", command = frame1).place(x=335,y=76)
        Button(P[frame],text="Guardar",bg="light blue", command=GuardarConfig1).place(x=220, y=yv)
        Button(P[frame], text="Cargar", bg="light blue", command = cargar1).place(x=400,y=25)
    elif(frame == 1):
        Button(P[frame], text="Aceptar", bg="light blue", command = frame2).place(x=335,y=76)
        Button(P[frame],text="Guardar",bg="light blue", command=GuardarConfig2).place(x=220, y=yv)
        Button(P[frame], text="Cargar", bg="light blue", command = cargar2).place(x=400,y=25)
    elif(frame == 2):
        Button(P[frame], text="Aceptar", bg="light blue", command = frame1).place(x=335,y=76)
        Button(P[frame],text="Guardar",bg="light blue", command=GuardarConfig3).place(x=220, y=yv)
        Button(P[frame], text="Cargar", bg="light blue", command = cargar3).place(x=400,y=25)
    elif(frame == 3):
        Button(P[frame], text="Aceptar", bg="light blue", command = frame1).place(x=335,y=76)
        Button(P[frame],text="Guardar",bg="light blue", command=GuardarConfig4).place(x=220, y=yv)
        Button(P[frame], text="Cargar", bg="light blue", command = cargar4).place(x=400,y=25)
        
    #P1 = Button(P[frame],text="Guardar",bg="light blue", command=GuardarConfig).place(x=220, y=yv)
    P2 = Button(P[frame],text="Iniciar",bg="light blue", command=iniciar).place(x=420, y=yv)
    #P3 = Button(P[frame],text="Detener Ejecución",bg="light blue", command=saludo).place(x=20, y=yv)
    raiz.geometry("500x" + str(yv+70))

#Ventana principal
raiz = tkinter.Tk()
raiz.title("Aplicación")
raiz.geometry("500x400")
nombre = StringVar()
TEP1 = StringVar()
TEP2 = StringVar()
TEP3 = StringVar()
TEP4 = StringVar()
TEP5 = StringVar()
TEP6 = StringVar()
TEP7 = StringVar()
TEP8 = StringVar()
TEP9 = StringVar()
TEP10 = StringVar()
TEP11 = StringVar()
TEP12 = StringVar()
TEP13 = StringVar()
TEP14 = StringVar()
TEP15 = StringVar()
TEP16 = StringVar()
TER1 = StringVar()
TER2 = StringVar()
TER3 = StringVar()
TER4 = StringVar()
TER5 = StringVar()
TER6 = StringVar()
TER7 = StringVar()
TER8 = StringVar()
TER9 = StringVar()
TER10 = StringVar()
TER11 = StringVar()
TER12 = StringVar()
TER13 = StringVar()
TER14 = StringVar()
TER15 = StringVar()
TER16 = StringVar()
TEL = [TEP1, TEP2, TEP3, TEP4, TEP5, TEP6, TEP7, TEP8, TEP9, TEP10, TEP11, TEP12, TEP13, TEP14, TEP15, TEP16]
TEN = [TER1, TER2, TER3, TER4, TER5, TER6, TER7, TER8, TER9, TER10, TER11, TER12, TER13, TER14, TER15, TER16]
CRP = StringVar()
CR = StringVar()
TE = StringVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
#Panel de pestañas

nb = ttk.Notebook(raiz)
nb.pack(fill="both", expand="yes")

p1 = Frame(nb)
#p1.config(bg="blue")
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)
p4 = ttk.Frame(nb)

P = [p1, p2, p3, p4]


nb.add(p1,text="Tiempo 1")
nb.add(p2,text="Tiempo 2")
nb.add(p3,text="Tiempo 3")
nb.add(p4,text="Tiempo 4")

#Elementos de pestaña p1
Label(p1,text="Nombre: ").place(x=20,y=30)
Button(p1, text="Cargar", bg="light blue", command = cargar1).place(x=400,y=25)
Entry(p1,textvariable=nombre, width=50).place(x=75,y=30)
Label(p1,text="Cantidad de Intervalos de Tiempo:").place(x=20,y=80)
Entry(p1,textvariable=CRP, width=18).place(x=210,y=80)
Button(p1, text="Aceptar", bg="light blue", command = frame1).place(x=335,y=76)


#Elementos de pestaña p2
Label(p2,text="Nombre: ").place(x=20,y=30)
Button(p2, text="Cargar", bg="light blue", command = cargar2).place(x=400,y=25)
Entry(p2,textvariable=nombre, width=50).place(x=75,y=30)
Label(p2,text="Cantidad de Intervalos de Tiempo:").place(x=20,y=80)
Entry(p2,textvariable=CRP, width=18).place(x=210,y=80)
Button(p2, text="Aceptar", bg="light blue", command = frame2).place(x=335,y=76)

#Elementos de pestaña p3
Label(p3,text="Nombre: ").place(x=20,y=30)
Button(p3, text="Cargar", bg="light blue", command = cargar3).place(x=400,y=25)
Entry(p3,textvariable=nombre, width=50).place(x=75,y=30)
Label(p3,text="Cantidad de Intervalos de Tiempo:").place(x=20,y=80)
Entry(p3,textvariable=CRP, width=18).place(x=210,y=80)
Button(p3, text="Aceptar", bg="light blue", command = frame3).place(x=335,y=76)

#Elementos de pestaña p4
Label(p4,text="Nombre: ").place(x=20,y=30)
Button(p4, text="Cargar", bg="light blue", command = cargar4).place(x=400,y=25)
Entry(p4,textvariable=nombre, width=50).place(x=75,y=30)
Label(p4,text="Cantidad de Intervalos de Tiempo:").place(x=20,y=80)
Entry(p4,textvariable=CRP, width=18).place(x=210,y=80)
Button(p4, text="Aceptar", bg="light blue", command = frame4).place(x=335,y=76)

raiz.mainloop()

