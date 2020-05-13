lista = [1, 2, 5, 7]
lista_animal = ["Cachorro", "Gato", "Elefante"]
print(lista)
print(lista_animal)

#Ordena a lista
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

#Ordena a lista de forma reversa
lista.reverse()
lista_animal.reverse()
print(lista)
print(lista_animal)

for x in lista:
    print(x)

for x in lista_animal:
    print(x)

if 'Lobo' in lista_animal:
    print("existe um lobo na lista")
else:
    print("não existe um lobo na lista. Será incluido.")
    lista_animal.append("Lobo")
    print(lista_animal)

#remove o ultimo elementos de dentro da list pela posição na lista
lista_animal.pop()
print(lista_animal)

#remove o elemento passado como parametro de dentro da list
lista_animal.remove("Elefante")
print(lista)

print(len(lista))
print(len(lista_animal))


print("-----")


tupla = (1, 10, 12, 14)
print(tupla)

#converte a lista em tupla
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

#converte a tupla em lista
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)