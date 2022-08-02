import tkinter
import sqlite3

bd = sqlite3.connect('/home/alca/Documentos/ClashRoluby/Juego/BDCLash.db')

ventana = tkinter.Tk()
cur = bd.cursor()

def guardar():
    velocidad = caja_velocidad.get().upper()
    sql ='INSERT INTO CARTAS (VELOCIDAD) VALUES ( {} );'
    cur.execute(sql.format())
    bd.commit()
    
caja_velocidad = tkinter.Entry(ventana)
caja_velocidad.pack()

boton1 = tkinter.Button(ventana, text = "Guardar", command = guardar)
boton1.pack()

ventana.mainloop()