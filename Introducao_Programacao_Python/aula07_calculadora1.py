#declarar uma classe

class Calculadora:
    #funciona como um metodo construtor
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    #declarar um metodo
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicaco(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b


if __name__ == "__main__":

    #instanciar uma classe
    calculadora = Calculadora(10, 2)

    print(calculadora.valor_a)
    print(calculadora.valor_b)

    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicaco())
    print(calculadora.divisao())