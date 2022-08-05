import sqlite3

bd = sqlite3.connect('/home/alca/Documentos/ClashRoluby/Juego/BDCLash.db')
c = bd.cursor()
c.execute('select * from CARTAS')
respuesta = c.fetchall()
for i in respuesta:
    print(('NOMBRE: '+ i[1]+ ' DANIO:'+ str(i[2])+ ' VIDA:'+ str(i[3])))
    vidanueva = input('Ingrese vida nueva: ')
    c.execute(f'update CARTAS set VIDA = {vidanueva} where ID = {i[0]};')
    bd.commit()
    