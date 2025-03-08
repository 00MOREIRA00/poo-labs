# Encapsulamento na Programação Orientada a Objetos

O encapsulamento é um dos pilares fundamentais da Programação Orientada a Objetos (POO). Ele permite que os desenvolvedores controlem o acesso aos dados e métodos de um objeto, protegendo a integridade dos dados e promovendo a modularidade do código.

## O que é Encapsulamento?

Encapsulamento é o processo de esconder os detalhes internos de um objeto e expor apenas o que é necessário. Isso é feito através de modificadores de acesso como público, privado e protegido. O encapsulamento ajuda a proteger os dados de acessos indevidos e a manter a integridade do objeto.

## Benefícios do Encapsulamento

* **Proteção dos Dados:** O encapsulamento protege os dados de acessos indevidos e modificações não autorizadas.
* **Modularidade:** Promove a modularidade do código, permitindo que diferentes partes do sistema sejam desenvolvidas e mantidas de forma independente.
* **Facilidade de Manutenção:** Facilita a manutenção do código, pois mudanças nos detalhes internos de uma classe não afetam outras partes do sistema.

## Exemplo de Encapsulamento

Vamos considerar um exemplo de uma classe `Carro` que utiliza encapsulamento para proteger seus atributos.

```python
class Carro:
    def __init__(self, marca, modelo):
        self.__marca = marca                # ATRIBUTO PRIVADO
        self.__modelo = modelo              # ATRIBUTO PRIVADO
        self.__velocidade = 0               # ATRIBUTO PRIVADO

    def acelerar(self, incremento):
        self.__velocidade += incremento     # MÉTODO PÚBLICO

    def frear(self, decremento):
        self.__velocidade -= decremento     # MÉTODO PÚBLICO

    def get_velocidade(self):
        return self.__velocidade            # MÉTODO PÚBLICO

    def get_marca(self):
        return self.__marca                 # MÉTODO PÚBLICO

    def get_modelo(self):
        return self.__modelo                # MÉTODO PÚBLICO
```

Neste exemplo, os atributos `__marca`, `__modelo` e `__velocidade` são privados e só podem ser acessados através dos métodos públicos `acelerar`, `frear`, `get_velocidade`, `get_marca` e `get_modelo`. Isso protege os atributos de acessos indevidos e garante que a velocidade do carro só possa ser alterada através dos métodos apropriados.

## Conclusão

O encapsulamento é uma ferramenta poderosa na POO que permite proteger os dados e promover a modularidade do código. Ao esconder os detalhes internos de um objeto e expor apenas o que é necessário, o encapsulamento facilita a manutenção, a reutilização e a integridade do código.
