from constants import ITEMS, MAX_WEIGHT
from algorithms.dynamic_programing import dp_algorithm
from algorithms.greedy import *
from tabulate import tabulate

def generate_output(algorithm):
    '''
    Esta funcion genera la salida del programa de manera automatica,
    solo debes pasar el algoritmo a utilizar
    '''
    result: list[Item] = algorithm(ITEMS)

    print(''.ljust(25, '-'))
    print(f'Peso maximo de la mochila: {MAX_WEIGHT}')
    print('Peso de la mochila:', sum([item.weight for item in result]))
    print('Contenido de la mochila:\n')
    print(tabulate(result, headers=['Nombre', 'Peso', 'Valor']))
    print(''.ljust(25, '-'))

def main():
    generate_output(h1_menor_peso)
    # generate_output(h2_mayor_valor)
    # generate_output(h3_mayor_cociente)
    # generate_output(dp_algorithm)

if __name__ == '__main__':
    main()
