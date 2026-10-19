
class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, objetivo):
        objetivo.vida -= self.ataque - objetivo.defensa

        print(
            f"{self.nombre} ataca a {objetivo.nombre} "
            f"y causa {self.ataque} de daño"
        )

        if objetivo.vida <= 0:
            print(f"{objetivo.nombre} ha sido derrotado")
        else:
            print(f"Vida restante: {objetivo.vida}")


jugador = Personaje("Caballero", 100, 10, 2)
enemigo = Personaje("Slime", 50, 5, 1)

while jugador.vida >= 0 and enemigo.vida >= 0:
    jugador.atacar(enemigo)
    enemigo.atacar(jugador) 
