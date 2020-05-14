#declarar uma classe
class Calculadora:
    
    #funciona como um metodo construtor
    def __init__(self):
        #faz com que não tenha necessidade de passar um valor como parametro no construtor
        pass

    #declarar um metodo
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicaco(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b


if __name__ == "__main__":
        
    #instanciar uma classe
    calculadora = Calculadora()

    print(calculadora.soma(10, 3))
    print(calculadora.subtracao(19, 2))
    print(calculadora.multiplicaco(20, 4))
    print(calculadora.divisao(11, 55))