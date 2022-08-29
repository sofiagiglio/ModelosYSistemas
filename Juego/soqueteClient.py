from tkinter import *
#Imports library
import socket

#Creates instance of 'Socket'
s = socket.socket()

def conectar():
    hostname = '192.168.88.20'
    port = 8080 #Server Port
    s.connect((hostname,port)) #Connects to server

def enviar():
    x = texto.get() #Gets the message to be sent
    s.send(x.encode()) #Encodes and sends message (x)

ventana = Tk()
texto = Entry(ventana)
boton = Button(ventana, text="Enviar", command=enviar)
texto.pack()
boton.pack()
ventana.mainloop()