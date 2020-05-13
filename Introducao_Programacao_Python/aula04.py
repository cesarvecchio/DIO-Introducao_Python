num = int(input("Entre com um numero: "))

for num in range(101):
     div = 0
     for x in range(1, num):
         resto = num % x

         if resto == 0:
             div += 1

if div == 2:
     print("O número {} é primo".format(num))
else:
     print("O numero {} não é primo".format(num))

print('-----')

nota1 = int(input("Entre com a nota 1: "))
while nota1 > 10:
    nota1 = int(input("Nota 1 invalida. Entre com a nota correta: "))

nota2 = int(input("Entre com a nota 2: "))
while nota2 > 10:
    nota2 = int(input("Nota 2 invalida. Entre com a nota correta: "))


nota3 = int(input("Entre com a nota 3: "))
while nota3 > 10:
    nota3 = int(input("Nota 3 invalida. Entre com a nota correta: "))


nota4 = int(input("Entre com a nota 4: "))
while nota4 > 10:
    nota4 = int(input("Nota 4 invalida. Entre com a nota correta: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print("Média da nota: {}".format(media))

print("Programa finalizado")