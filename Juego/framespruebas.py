import tkinter

ventana = tkinter.Tk()

f1 = tkinter.Frame(ventana)
f1.grid(column=0, row=0)
f2 = tkinter.Frame(ventana)
f2.grid(column=0, row=1)

etiqueta = tkinter.Label(f1, text = "¡Welcome to Roluby Clash!", font = "Arial 30", bg = "pink")
etiqueta.pack()

cajaTexto= tkinter.Entry(f1)
cajaTexto.pack()

boton1 = tkinter.Button(f2, text = "Let's go ;)", bg = "pink")
boton1.pack()

ventana.mainloop() 