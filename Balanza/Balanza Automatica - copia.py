import serial
import re
import sys
from tkinter import *
from tkinter import messagebox
import tkinter
import threading
from pynput.keyboard import Key, Controller



def main():
    global port
    t = threading.currentThread()
    try:
        ser = serial.Serial(port)  
        print(ser.name)
    except serial.serialutil.SerialException:
        print("No se ha podido comunicar con la balanza, revise que esta este conectada y el puerto de comunicacion es el correcto.")
        sys.exit()
    keyboard = Controller()
    while getattr(t, "do_run", True):
        s = ser.read(15)
        peso = s.decode('utf-8')
        peso_filtrado = re.findall("\d+\.\d+", peso)[0]
        keyboard.type(peso_filtrado)
        keyboard.press(Key.down)
    ser.close()

def puertos_serial():
    global puertos_dispon
    puertos = ['COM%s' % (i + 1) for i in range(256)]
    puertos_dispon = []
    for puerto in puertos:
        try:
            s = serial.Serial(puerto)
            s.close()
            puertos_dispon.append(puerto)
        except (OSError, serial.SerialException):
            pass
    if puertos_dispon == []:
        puertos_dispon.append("")
        messagebox.showinfo(message='La balanza no esta conectada')

def update_option_menu():
        global com_ports, puertos_dispon, variable
        puertos_serial()
        menu = com_ports["menu"]
        menu.delete(0,"end")
        for string in puertos_dispon:
            menu.add_command(label=string, 
                             command=lambda value=string: variable.set(value))

def leer_balanza():
    global hiloSerial, variable, port
    port = variable.get()
    print(port)
    hiloSerial = threading.Thread(target = main)
    hiloSerial.start()

def on_close():
    global hiloSerial, top
    try:
        hiloSerial.do_run = False
    except:
        pass
    #hiloSerial.join()
    top.destroy()
    sys.exit()
    



top = tkinter.Tk()
top.protocol("WM_DELETE_WINDOW", on_close)
top.resizable(False, False)
top.geometry('300x300')
top.title('Balanza Automatica')

puertos_serial()

variable = StringVar(top)
variable.set(puertos_dispon[0])

com_ports = OptionMenu(top, variable, *puertos_dispon)
com_ports.pack()

button_refresh = tkinter.Button(top, text="Refrescar", command=update_option_menu)
button_refresh.pack()

button_correr = tkinter.Button(top, text="Correr", command=leer_balanza)
button_correr.pack()




top.mainloop()
    
#Ejecucion del codigo main    
#main()
#puertos_serial()
