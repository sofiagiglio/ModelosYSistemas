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