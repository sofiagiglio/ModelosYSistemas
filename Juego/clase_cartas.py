from bd_utils import traer_carta_random
from urllib.request import Request, urlopen
from PIL import ImageTk, Image

class Jugador:
    carta = {'vida': 0, 'danio': 0, 'foto': ''}
    
    
    def pegar(self, oponente):
        if oponente.carta['vida'] > 0:
            oponente.carta['vida'] -= self.carta['danio']
        else:
            print("El Jugador no tiene vida")
            
    def preparar_carta(self):
        datos = traer_carta_random()
        self.carta['vida'] = datos[1]
        self.carta['danio'] = datos[2]

        url_final = datos[0]
        vida = datos[1]
        danio = datos[2]
        req = Request(datos[0], headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(req).read()
        #self.carta['foto'] = ImageTk.PhotoImage(data=raw_data)
    
    def __init__(self):
        self.preparar_carta()
