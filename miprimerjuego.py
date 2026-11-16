
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
#clase mago (herencia)
class Mago(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, mana):
        super().__init__(nombre, vida, ataque, defensa)
        self.mana = mana
    def atacar_magia(self, objetivo):
        if self.mana >= 5:
            self.mana -= 5
            objetivo.vida -= self.ataque * 2 - objetivo.defensa
            print(
                f"{self.nombre} lanza un hechizo a {objetivo.nombre} "
                f"y causa {self.ataque * 2} de daño"
            )
        else:
            print(f"{self.nombre} no tiene suficiente mana para atacar")