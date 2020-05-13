a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print("---------- str()")
# 'str() = irá converter uma variavel para STRING'
print("Soma: " + str(soma))
print("Subtação: " + str(subtracao))
print("Multiplicação: " + str(multiplicacao))
print("Divisão: " + str(divisao))
print("Resto da divisão: " + str(resto))

print("---------- .format()")
# '...{}'.format() = irá formatar a string colocando o valor passado como parametro no lugar das '{}'
print("Soma: {}".format(soma))
print("Subtação: {}".format(subtracao))
print("Multiplicação: {}".format(multiplicacao))
print("Divisão: {}".format(divisao))
print("Resto da divisão: {}".format(resto))