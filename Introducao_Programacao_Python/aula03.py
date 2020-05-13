# print("-----")
# a = int(input("primeiro valor: "))
# b = int(input("segundo valor: "))
# c = int(input("terceiro valor: "))

# if a > b and a > c:
#     print("O maior numero é {}".format(a))
# elif b> a and b > c:
#     print("O maior numero é {}".format(b))
# else:
#     print("O maior numero é {}".format(c))

# print('Final if/elif/else')


# print("-----")

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print("Foi digitado um numero par")
# else: 
#     print("Nenhum numero par foi digitado")

print("Final numero par ou impar")


print("-----")

a = int(input("Primeiro bimestre: "))
b = int(input("Segundo bimestre: "))
c = int(input("Terceiro bimestre: "))
d = int(input("Quarto bimestre: "))

media = (a + b + c + d) / 4

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print("media: {}".format(media))
else:
    print("Foi informado alguma nota errada")