import tkinter
from PIL import ImageTk, Image
from bd_utils import traer_url_foto_por_id, traer_carta_random
from urllib.request import Request, urlopen
import login

l = login.Login()


ventana = tkinter.Tk()
ventana.title("Battle cards Roluby<3")

def preparar_carta():
    datos = traer_carta_random()
    url_final = datos[0]
    vida = datos[1]
    danio = datos[2]
    velocidad = datos[4]
    req = Request(url_final, headers={'User-Agent': 'Mozilla/5.0'})
    raw_data = urlopen(req).read()
    photo = ImageTk.PhotoImage(data=raw_data)
    print(f'Carta sorteada para jugador DAÑO: {danio} VIDA: {vida} VELOCIDAD: {velocidad}')
    return (photo, vida, danio, velocidad)


f1 = tkinter.Frame(ventana)
f1.grid(column=0, row=0)
f2 = tkinter.Frame(ventana)
f2.grid(column=1, row=0)
f3 = tkinter.Frame(ventana)
f3.grid(column=2, row=0)

carta1 = preparar_carta()
ph1 = carta1[0]
l1 = tkinter.Label(f1, image=ph1)
l1.grid(column=0, row=0)

carta2 = preparar_carta()
ph2 = carta2[0]
lomo = ImageTk.PhotoImage(Image.open('lomo_clash.png'))
l2 = tkinter.Label(f3, image=lomo)
l2.grid(column=0, row=0)

boton1 = tkinter.Button(f2, text = "Vida", command = lambda: print("La vida de j1 es _ y la de j2 es _"))
boton1.pack()

boton2 = tkinter.Button(f2, text = "Daño", command = lambda: print("El daño de j1 es _ y la de j2 es _"))
boton2.pack()

boton2 = tkinter.Button(f2, text = "Velocidad", command = lambda: print("La velocidad de j1 es _ y la de j2 es _"))
boton2.pack()

boton2 = tkinter.Button(f2, text = "Rendirse", command = lambda: print("_ se rindió"))
boton2.pack()

ventana.mainloop()