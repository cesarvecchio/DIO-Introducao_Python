# #importa todas as classes e metodos desse arquivo
# import aula07_televisao

#importa apenas a classe selecionada
from aula07_televisao import Televisao
from aula07_calculadora1 import Calculadora
from aula08_contador_letras import contador_letras, teste

if __name__ == "__main__":
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())

    lista = ["cachorro", "gato", "elefante"]
    total_letras = contador_letras(lista)
    print("total de letras por palavras de lista: {}".format(total_letras))
    print(teste())