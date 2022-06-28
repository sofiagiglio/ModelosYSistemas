import sqlite3

bd = sqlite3.connect('/home/alca/Escritorio/Ortiz_Balbuena_ProgII/JuegoClash/BDCLash.db')
c = bd.cursor()
c.execute('select * from CARTAS')
respuesta = c.fetchall()
for i in respuesta:
    print(i[1]+ ' vida: ' + str(i[3]))
    vidanueva = input('Ingrese vida nueva: ')
    c.execute(f'update CARTAS set VIDA = {vidanueva} where ID = {i[0]}')
    bd.commit()
    