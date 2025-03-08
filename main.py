class Personagem:
    def __init__(self, nome):
        self.vida = 100
        self.dano = 10
        self.defesa = 5
        self.velocidade = 5
        self.nome = nome
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}")

    def atacar(self):
        print("Atacando")
    
    def defender(self):
        print("Defendendo")
    
    def mover(self):
        print("Movendo")
    

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.mana = 100
        self._arma = "Espada"
        self.__fraqueza = "Fogo"
    
    def feitico(self):
        print("Lançando feitiço")
    
    def get_fraqueza(self):
        return self.__fraqueza
        



# Persoangem 1 
personagem_1 = Personagem("Clementino de Jesus")
personagem_1.apresentar()

print(personagem_1.dano)


# Mago 
mago_1 = Mago("Belveder")
mago_1.apresentar()
print(mago_1.dano)
print(mago_1.get_fraqueza())









