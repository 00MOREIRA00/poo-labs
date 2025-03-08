# Abstração na Programação Orientada a Objetos

A abstração é um dos pilares fundamentais da Programação Orientada a Objetos (POO). Ela permite que os desenvolvedores modelem conceitos do mundo real de forma simplificada, focando nos aspectos essenciais e ignorando os detalhes desnecessários.

## O que é Abstração?

Abstração é o processo de identificar os atributos e comportamentos essenciais de um objeto e criar uma representação simplificada desse objeto em uma classe. A abstração ajuda a reduzir a complexidade do sistema, permitindo que os desenvolvedores se concentrem nas funcionalidades principais sem se preocupar com os detalhes internos.

## Benefícios da Abstração

* **Redução da Complexidade:** Ao focar apenas nos aspectos essenciais, a abstração torna o sistema mais fácil de entender e manter.
* **Reutilização de Código:** Classes abstratas podem ser usadas como base para outras classes, promovendo a reutilização de código.
* **Facilidade de Manutenção:** A abstração permite que mudanças nos detalhes internos de uma classe não afetem outras partes do sistema.

## Exemplo de Abstração

Vamos considerar um exemplo de uma classe abstrata `Forma` e suas subclasses `Circulo` e `Retangulo`.

```python
from abc import ABC, abstractmethod

class Forma(ABC):                          # CLASSE ABSTRATA
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Forma):                      # SUBCLASSE
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio * self.raio

    def perimetro(self):
        return 2 * 3.14 * self.raio

class Retangulo(Forma):                    # SUBCLASSE
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)
```

Neste exemplo, `Forma` é uma classe abstrata que define os métodos `area` e `perimetro`, mas não fornece implementações para eles. As subclasses `Circulo` e `Retangulo` implementam esses métodos de acordo com suas próprias características.

## O que acontece se uma subclasse não implementar um método abstrato?

Se uma subclasse não implementar todos os métodos abstratos definidos na classe base, o Python levantará um erro TypeError quando você tentar instanciar essa subclasse. Isso garante que todas as subclasses forneçam implementações para os métodos essenciais definidos na classe base abstrata.

## Conclusão

A abstração é uma ferramenta poderosa na POO que permite simplificar a modelagem de sistemas complexos. Ao focar nos aspectos essenciais e ignorar os detalhes desnecessários, a abstração facilita a compreensão, manutenção e reutilização do código.
