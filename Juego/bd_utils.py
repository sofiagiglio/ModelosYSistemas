import sqlite3
import random

bd = sqlite3.connect('/home/alca/Documentos/ClashRoluby/Juego/BDCLash.db')
c = bd.cursor()

def traer_carta_random():
    c.execute("SELECT ID FROM CARTAS")
    ids = c.fetchall()
    pos = random.randint(0,len(ids)-1)
    #print(ids[pos][0])
    id_busqueda = ids[pos][0]
    c.execute(f"SELECT URLFOTO, VIDA, DANIO FROM CARTAS WHERE ID = {id_busqueda} ")
    resp = c.fetchall()
    url = resp[0][0]
    vida = resp[0][1]
    danio = resp[0][2]
    lista = url.split("/")
    pre = 'https://www.deckshop.pro/img/card_ed/'
    post = '.png'
    url_foto = pre + lista[len(lista)-1] + post
    return (url_foto, vida, danio)


def traer_url_foto_por_id(id_busqueda):
    c.execute(f"SELECT URLFOTO FROM CARTAS WHERE ID = {id_busqueda} ")
    resp = c.fetchall()
    url = resp[0][0]
    lista = url.split("/")
    pre = 'https://www.deckshop.pro/img/card_ed/'
    post = '.png'
    url_foto = pre + lista[len(lista)-1] + post
    return url_foto

def crear_usuario(nombre, usr, passw):
    #tomo usr y passw y lo guardo en la base de datos
    c.execute(f'INSERT INTO USUARIOS (NOMBRE, USUARIO, CONTRASENIA) VALUES("{nombre}", "{usr}","{passw}")' )
    bd.commit()

def buscar_usuario(usr):
    #responder true si existe el usr
    pass

def loguear(usr, passw):
    #tomo usr y passw y me fijo si existe en la base de datos y si coincide con la pass
    #devuelvo true o false según si coincide la passw
    #return True/False
    pass

