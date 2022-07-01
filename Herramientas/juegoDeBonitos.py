class Jugador:
    energia = 100
    armadura = 100
    poder = 10
    
    def __init__(self, nom, **kwargs):
        self.nombre = nom
        try:
            self.energia = kwargs['energia']
        except:
            pass
            
    def pegar(self, oponente):
        if oponente.armadura < 0:
            oponente.energia -= self.poder * 0.5
        else:
            oponente.armadura -= self.poder * 0.1
        print("Jugador {} dañado, armadura: {}, energía: {}".format(oponente.nombre, oponente.armadura, oponente.energia))
    
    def cargar_energia(self, cantidad):
        self.energia += cantidad
    
    def entrenar(self, horas):
        self.poder += horas*0.5
        print("El poder de {} subió a {}".format(self.nombre, self.poder))
    
j1 = Jugador("Esteban", energia=1000)
j2 = Jugador("Luis")
