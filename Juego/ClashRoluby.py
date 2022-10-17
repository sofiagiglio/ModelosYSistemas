import tkinter
from PIL import ImageTk, Image
from bd_utils import traer_carta_random
from urllib.request import Request, urlopen
import login
from functools import partial
#from itertools import cycle

l = login.Login()

class Pantalla:
    def __init__(self):
        self.j1 = Jugador()
        print(f'j1 vida = {self.j1.vida}')
        
        self.j2 = Jugador()
        print(f'j2 vida = {self.j2.vida}')
        self.ventana = tkinter.Tk()
        self.ventana.title("Battle cards Roluby<3")
        self.f1 = tkinter.Frame(self.ventana)
        self.f1.grid(column=0, row=0)
        f2 = tkinter.Frame(self.ventana)
        f2.grid(column=1, row=0)
        self.f3 = tkinter.Frame(self.ventana)
        self.f3.grid(column=2, row=0)
        f4 = tkinter.Frame(self.ventana)
        f4.grid(column=0, row=1)
        f5 = tkinter.Frame(self.ventana)
        f5.grid(column=2, row=1)
        lomo = ImageTk.PhotoImage(Image.open('lomo_clash.png'))
        self.photo = self.sacar_cartas(self.j1)
        self.l1 = tkinter.Label(self.f1)
        self.l1.grid(column=0, row=0)
        self.l2 = tkinter.Label(self.f3, image=lomo)
        self.l2.grid(column=0, row=0)
        self.poner_foto(self.l1,1)
        
        boton1 = tkinter.Button(f2, text = "Vida", command = partial(self.jugar_mano, self.j1.comp_vida, self.j2))
        boton1.pack()
        boton2 = tkinter.Button(f2, text = "Daño", command = partial(self.jugar_mano, self.j1.comp_danio, self.j2))
        boton2.pack()
        boton3 = tkinter.Button(f2, text = "Velocidad", command = partial(self.jugar_mano, self.j1.comp_velocidad, self.j2))
        boton3.pack()
        self.boton4 = tkinter.Button(f2, text = "Rendirse", command = partial(self.jugar_mano, self.j1.rendirse, None))
        self.boton4.pack()
        self.etiqueta1 = tkinter.Label(f4, text = f'NOMBRE: {self.j1.nombre}')
        self.etiqueta1.pack()
        self.etiqueta2 = tkinter.Label(f4, text = f'DAÑO: {self.j1.danio}')
        self.etiqueta2.pack()
        self.etiqueta3 = tkinter.Label(f4, text = f'VIDA: {self.j1.vida}')
        self.etiqueta3.pack()
        self.etiqueta4 = tkinter.Label(f4, text = f'VELOCIDAD: {self.j1.velocidad}')
        self.etiqueta4.pack()
        self.etiqueta5 = tkinter.Label(f4, text = f'PUNTOS: {self.j1.puntos}')
        self.etiqueta5.pack()
        self.etiqueta6 = tkinter.Label(f5, text = "")
        self.etiqueta6.pack()
        
        self.ventana.mainloop()
    
    def jugar_mano(self,funcion_jugador, atributo_jugada):
        respuesta = funcion_jugador(atributo_jugada)
        self.etiqueta1.config(text = f'NOMBRE: {self.j1.nombre}')
        self.etiqueta2.config(text = f'DAÑO: {self.j1.danio}')
        self.etiqueta3.config(text = f'VIDA: {self.j1.vida}')
        self.etiqueta4.config(text = f'VELOCIDAD: {self.j1.velocidad}')
        self.etiqueta5.config(text = f'PUNTOS: {self.j1.puntos}')
        self.etiqueta6.config(text = f'MENSAJE: {respuesta["mensaje"]}')
        self.j1.preparar_carta()
        self.j2.preparar_carta()
        print(self.j2.url_final)
        self.boton4.config(state=tkinter.DISABLED)
        self.photo = self.sacar_cartas(self.j1)
        self.photo2 = self.sacar_cartas(self.j2)
        self.poner_foto(self.l1,1)
    
    def sacar_cartas(self, jugador):
        req = Request(jugador.url_final, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(req).read()
        p = ImageTk.PhotoImage(data=raw_data)
        return p
        
    def poner_foto(self, label, jug):
        if jug == 1:
            label.config(image=self.photo)
        else:
            label.config(image=self.photo2)
    
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
            self.respuesta["mensaje"] = "Ganó por: " + str(self.danio - oponente.danio)
            print("Ganó por: " + str(self.danio - oponente.danio))
        else:
            oponente.puntos += 20
            print("Perdió por: " + str(oponente.danio - self.danio))
            self.respuesta["mensaje"] = "Perdió por: " + str(oponente.danio - self.danio)
        self.respuesta["puntos"] = self.puntos
        return self.respuesta
            
    def comp_velocidad(self, oponente):
        if self.velocidad > oponente.velocidad:       
            self.puntos += 20            
            self.respuesta["mensaje"] = "Ganó por: " + str(self.velocidad - oponente.velocidad)
            print("Ganó por: " + str(self.velocidad - oponente.velocidad))
        else:
            oponente.puntos += 20
            print("Perdió por: " + str(oponente.velocidad - self.velocidad))
            self.respuesta["mensaje"] = "Perdió por: " + str(oponente.velocidad - self.velocidad)
        self.respuesta["puntos"] = self.puntos
        return self.respuesta
            
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
    p = Pantalla()