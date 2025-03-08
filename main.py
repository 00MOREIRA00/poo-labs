from abc import ABC, abstractmethod

class Personagem(ABC):
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
    
    @abstractmethod
    def exibir_informacoes(self):
        pass

    @staticmethod
    def criar_personagem(tipo, nome):
        if tipo == "Mago":
            return Mago(nome)
        elif tipo == "Barbaro":
            return Barbaro(nome)
        else:
            raise ValueError("Tipo de personagem desconhecido")

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.mana = 100
        self._arma = "Cajado"
        self.__fraqueza = "Fogo"
    
    def feitico(self):
        print("Lançando feitiço")
    
    def get_fraqueza(self):
        return self.__fraqueza
    
    def exibir_informacoes(self):
        return f"Nome: {self.nome} e Vida: {self.vida}"

class Barbaro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.furia = 100
        self._arma = "Clava"
        self.__fraqueza = "Magia"
    
    def clava(self):
        print("Usando Clava")
    
    def get_fraqueza(self):
        return self.__fraqueza
    
    def exibir_informacoes(self):
        return f"Nome: {self.nome} e Vida: {self.vida}"
    

# def exibir_informacoes(personagem):
#     return personagem.exibir_informacoes()




# # Criação de personagens usando o método estático
# personagem_1 = Personagem.criar_personagem("Mago", "Belveder")
# print(personagem_1.exibir_informacoes())
# print(personagem_1.get_fraqueza())

# personagem_2 = Personagem.criar_personagem("Barbaro", "Conan")
# print(personagem_2.exibir_informacoes())

# print(exibir_informacoes(personagem_1))



personagem_barbaro = Personagem.criar_personagem("Barbaro", "Conan")
personagem_barbaro.clava()
print(personagem_barbaro.vida)








