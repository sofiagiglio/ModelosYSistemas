import tkinter
from PIL import ImageTk, Image
from bd_utils import traer_url_foto_por_id, traer_carta_random
from urllib.request import Request, urlopen
import login
from functools import partial
from itertools import cycle

l = login.Login()

class Pantalla:
    def __init__(self):
        self.j1 = Jugador()
        self.j2 = Jugador()
        ventana = tkinter.Tk()
        ventana.title("Battle cards Roluby<3")
        self.f1 = tkinter.Frame(ventana)
        self.f1.grid(column=0, row=0)
        f2 = tkinter.Frame(ventana)
        f2.grid(column=1, row=0)
        f3 = tkinter.Frame(ventana)
        f3.grid(column=2, row=0)
        f4 = tkinter.Frame(ventana)
        f4.grid(column=0, row=1)
        f5 = tkinter.Frame(ventana)
        f5.grid(column=2, row=1)
        self.l1 = tkinter.Label(self.f1)
        self.sacar_cartas()
        lomo = ImageTk.PhotoImage(Image.open('lomo_clash.png'))
        self.l2 = tkinter.Label(f3, image=lomo)
        self.l2.grid(column=0, row=0)

        boton1 = tkinter.Button(f2, text = "Vida", command = partial(self.jugar_mano, self.j1.comp_vida, self.j2))
        boton1.pack()
        boton2 = tkinter.Button(f2, text = "Daño", command = partial(self.jugar_mano, self.j1.comp_danio, self.j2))
        boton2.pack()
        boton3 = tkinter.Button(f2, text = "Velocidad", command = partial(self.jugar_mano, self.j1.comp_velocidad, self.j2))
        boton3.pack()
        boton4 = tkinter.Button(f2, text = "Rendirse", command = partial(self.jugar_mano, self.j1.rendirse, None))
        boton4.pack()

        etiqueta1 = tkinter.Label(f4, text = f'NOMBRE: {self.j1.nombre}')
        etiqueta1.pack()
        etiqueta2 = tkinter.Label(f4, text = f'DAÑO: {self.j1.danio}')
        etiqueta2.pack()
        etiqueta3 = tkinter.Label(f4, text = f'VIDA: {self.j1.vida}')
        etiqueta3.pack()
        etiqueta4 = tkinter.Label(f4, text = f'VELOCIDAD: {self.j1.velocidad}')
        etiqueta4.pack()
        self.etiqueta5 = tkinter.Label(f4, text = f'PUNTOS: {self.j1.puntos}')
        self.etiqueta5.pack()
        self.etiqueta6 = tkinter.Label(f5, text = "")
        self.etiqueta6.pack()
        
        ventana.mainloop()
    
    def jugar_mano(self,funcion_jugador, atributo_jugada):
        respuesta = funcion_jugador(atributo_jugada)
        self.etiqueta5.config(text = f'PUNTOS: {self.j1.puntos}')
        self.etiqueta6.config(text = f'MENSAJE: {respuesta["mensaje"]}')
        j1.preparar_carta()
        j2.preparar_carta()
        self.sacar_cartas()
    
    def sacar_cartas(self):
        req = Request(self.j1.url_final, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(req).read()
        photo = ImageTk.PhotoImage(data=raw_data, master=self.l1)
        self.l1.config(image=photo)
        self.l1.grid(column=0, row=0)
        


    
class Jugador:
    def __init__(self):
        self.puntos = 0
        self.preparar_carta()
        self.respuesta = {
            "puntos": 0,
            "mensaje": "",
            }
    def comp_vida(self, oponente):
        if self.vida > oponente.vida:       
            self.puntos += 20            
            self.respuesta["mensaje"] = "Ganó por: " + str(self.vida - oponente.vida)
            print("Ganó por: " + str(self.vida - oponente.vida))
        else:
            oponente.puntos += 20
            print("Perdió por: " + str(oponente.vida - self.vida))
            self.respuesta["mensaje"] = "Perdió por: " + str(oponente.vida - self.vida)
        self.respuesta["puntos"] = self.puntos
        return self.respuesta
    
    def comp_danio(self, oponente):
        if self.danio > oponente.danio:
            self.puntos += 20
            print("Ganó por: " + str(self.danio - oponente.danio))
        else:
            oponente.puntos += 20
            print("Perdió por: " + str(oponente.danio - self.danio))
            
    def comp_velocidad(self, oponente):
        if self.velocidad > oponente.velocidad:
            self.puntos += 20
            print("Ganó por: " + str(self.velocidad - oponente.velocidad))
        else:
            oponente.puntos += 20
            print("Perdió por: " + str(oponente.velocidad - self.velocidad))
            
    def rendirse(self):
        if True:
            self.puntos -= 10
            print("Se rindió. El juego empieza de nuevo")
            self.preparar_carta
            
            
    def preparar_carta(self):
        datos = traer_carta_random()
        self.url_final = datos[0]
        self.vida = datos[1]
        self.danio = datos[2]
        self.velocidad = datos[3]
        self.nombre = datos[4]

if __name__ == "__main__":
    j1 = Jugador()
    print(j1.vida)
    j2 = Jugador()
    print(j2.vida)
    p = Pantalla()