conjunto = {1, 2, 3, 4}
#adiciona um elemento ao conjunto
conjunto.add(5)
#remove um elemento de um conjunto
conjunto.discard(2)

conjunto2 = {5, 6, 7, 8}

#uni um conjunto ao outro
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto)
print(conjunto2)
print(conjunto_uniao)

#mostra o valor que se repita nos dois conjuntos
conjunto_intersecao = conjunto.intersection(conjunto2)
print(conjunto_intersecao)

#mostra os numeros que sejam diferentes dos numeros do conjunto passado como parametro
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(conjunto_diferenca)
print(conjunto_diferenca2)

#mostra os valores diferentes entre os dois conjuntos
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_diff_simetrica)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)


lista = ['cachorro', 'gato', 'gato', 'elefante']
#converte lista para conjunto
conjunto_animais = set(lista)
print(lista)
print(conjunto_animais)

#converte conjunto para lista
lista_animais = list(conjunto_animais)
print(lista_animais)
