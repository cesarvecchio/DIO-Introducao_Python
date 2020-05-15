
lista = [1, 10]

try:
    arquivo = open("teste.txt", 'r')
    text = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    # x = a
except ZeroDivisionError:
    print("Não é possivel realizar uma divisão por 0")
except ArithmeticError:
    print("Houve um erro ao realizar uma operação aritmética")
except IndexError:
    print("Erro ao acessar um indice inválidade da lista")
except BaseException as ex:
    print(ex)
else:
    print("Executa quando não ocorre exceção")
finally:
    print("Sempre executa")
    print("Fechando arquivo")
    arquivo.close()