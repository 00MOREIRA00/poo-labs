# Programação Orientada a Objetos 

Surgiu como uma forma de alternativa às características da programação estruturada, assim como fazer manuseio do mundo real. Ele se baseia em Classes e Objetos.

Exemplo: Carro

O carro é um objeto, suas características são atributos e suas ações seus métodos. 

* Classe: É um conjunto de características e comportamentos que definem um conjunto de objetos que pertencem à classe. É como um modelo ou uma planta para criar objetos.

* Objeto: É uma instância de uma classe, ou seja, é algo que foi criado do modelo da classe.

## Pilares do POO 

Os pilares da Programação Orientada a Objetos são fundamentais para entender como essa abordagem funciona. Eles são:

* Encapsulamento: É o princípio de esconder os detalhes internos de um objeto e expor apenas o que é necessário. Isso é feito através de modificadores de acesso como público, privado e protegido.
  * Exemplo: Em uma classe `Carro`, os atributos `velocidade` e `combustível` podem ser privados e acessados apenas através de métodos públicos.

* Herança: É o mecanismo pelo qual uma classe pode herdar características (atributos e métodos) de outra classe. A classe que herda é chamada de subclasse, e a classe da qual ela herda é chamada de superclasse.
  * Exemplo: Uma classe `Veiculo` pode ser a superclasse de `Carro` e `Moto`, onde `Carro` e `Moto` herdam atributos e métodos de `Veiculo`.

* Polimorfismo: É a capacidade de um objeto ser tratado como instâncias de diferentes classes, permitindo que um método tenha diferentes implementações.
  * Exemplo: Um método `mover` pode ser implementado de diferentes formas em classes `Carro` e `Avião`.

* Abstração: É o processo de simplificar a complexidade do mundo real, modelando classes que representam conceitos abstratos e escondendo detalhes desnecessários.
  * Exemplo: Uma classe `Pagamento` pode ser abstrata e ter subclasses como `PagamentoCartao` e `PagamentoDinheiro`, cada uma implementando o método `processar_pagamento` de forma diferente.

## Exemplo

Exemplo de criação de Classe.

```python
class Pessoa:                              # CLASSE
    def __init__(self, nome):
        self.nome = nome                    # ATRIBUTO
        self.bracos = 2                     # ATRIBUTO
        self.pernas = 2                     # ATRIBUTO
        
    def andar(self):                        # MÉTODO
        print("Andando")
    
    def falar(self):                        # MÉTODO
        print("Falando")
```

Essa classe é um objeto pessoa, que recebe como atributos alguns elementos que possui como nome, quantidade de braços e quantidade de pernas. Possui também alguns métodos que pode realizar que são ações como andar e falar. Ou seja, é uma abstração da vida real.
