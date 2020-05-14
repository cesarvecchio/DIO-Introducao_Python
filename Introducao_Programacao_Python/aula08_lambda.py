contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', "gato", 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b

subtracao = lambda a, b: a - b
print(soma(1, 2))
print(subtracao(1, 2))


calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora["multiplicacao"]
divisao = calculadora["divisao"]

print(soma(1, 4))
print(subtracao(4, 4))
print(multiplicacao(1, 100))
print(divisao(1, 3))