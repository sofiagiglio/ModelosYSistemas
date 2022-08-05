import sqlite3

bd = sqlite3.connect('/home/alca/Documentos/ClashRoluby/Juego/BDCLash.db')
c = bd.cursor()
c.execute('select * from CARTAS')
respuesta = c.fetchall()
for i in respuesta:
    print('NOMBRE: '+ i[1]+ ' DANIO:'+ str(i[2]))
    velocidad = input('ingrese velocidad: ')
    c.execute(f'update CARTAS set VELOCIDAD = ({velocidad})where ID = {i[0]};')
    bd.commit()