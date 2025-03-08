# Herança na Programação Orientada a Objetos

A herança é um dos pilares fundamentais da Programação Orientada a Objetos (POO). Ela permite que uma classe herde atributos e métodos de outra classe, promovendo a reutilização de código e a criação de hierarquias de classes.

## O que é Herança?

Herança é o mecanismo pelo qual uma classe (subclasse) pode herdar características (atributos e métodos) de outra classe (superclasse). A subclasse pode adicionar novos atributos e métodos ou sobrescrever os métodos existentes da superclasse.

## Benefícios da Herança

* **Reutilização de Código:** A herança permite que o código existente seja reutilizado em novas classes, reduzindo a duplicação de código.
* **Hierarquia de Classes:** Facilita a criação de hierarquias de classes, onde classes mais específicas herdam características de classes mais genéricas.
* **Facilidade de Manutenção:** Alterações na superclasse são automaticamente propagadas para as subclasses, facilitando a manutenção do código.

## Exemplo de Herança

Vamos considerar um exemplo de uma classe `Veiculo` e suas subclasses `Carro` e `Moto`.

```python
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"O {self.modelo} está acelerando")

    def frear(self):
        print(f"O {self.modelo} está freando")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def abrir_porta(self):
        print(f"Abrindo {self.portas} portas do {self.modelo}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def empinar(self):
        print(f"A {self.modelo} está empinando")
```

Neste exemplo, `Veiculo` é a superclasse que define os métodos `acelerar` e `frear`. As subclasses `Carro` e `Moto` herdam esses métodos e adicionam seus próprios atributos e métodos específicos (`portas` e `abrir_porta` para `Carro`, `cilindradas` e `empinar` para `Moto`).

## Conclusão

A herança é uma ferramenta poderosa na POO que permite a reutilização de código e a criação de hierarquias de classes. Ao herdar características de uma superclasse, as subclasses podem adicionar ou modificar funcionalidades, promovendo a flexibilidade e a manutenção do código.
