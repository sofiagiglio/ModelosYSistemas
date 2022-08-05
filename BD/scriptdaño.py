import sqlite3

bd = sqlite3.connect('')
c = bd.cursor()
c.execute('select * from CARTAS')
respuesta = c.fetchall()
for i in respuesta:
    print(i[1]+ ' daño: ' + str(i[2]))
    dañonuevo = input('Ingrese daño nuevo: ')
    c.execute(f'update CARTAS set DANIO = {dañonuevo} where ID = {i[0]}')
    bd.commit()