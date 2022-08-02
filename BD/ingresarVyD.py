import tkinter
import sqlite3

bd = sqlite3.connect('/home/alca/Documentos/ClashRoluby/Juego/BDClash.bd')

ventana = tkinter.Tk()
cur = bd.cursor()

def guardar():
    nombre = caja_nombre.get().upper()
    danio = int(caja_danio.get())
    vida = int(caja_vida.get())
    sql ='INSERT INTO CARTAS (NOMBRE, DANIO, VIDA) VALUES ("{}", {}, {});'
    cur.execute(sql.format())
    bd.commit()
    
caja_nombre = tkinter.Entry(ventana)
caja_nombre.pack()

caja_danio = tkinter.Entry(ventana)
caja_danio.pack()

caja_vida = tkinter.Entry(ventana)
caja_vida.pack()

boton1 = tkinter.Button(ventana, text = "Guardar", command = guardar)
boton1.pack()

ventana.mainloop()