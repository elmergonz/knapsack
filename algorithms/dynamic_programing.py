from constants import MAX_WEIGHT
from models.item import Item
import math


def dp_algorithm(items: list) -> list:
    '''
    Este algoritmo usa el metodo de fuerza bruta usando
    una memoria dinamica para optimizar el resultado
    '''

    # En esta lista almacenamos todas las combinaciones que son menores al peso maximo
    all_sums: dict[float, list[Item]] = {}

    # Esta variable almacena el tamaño de la lista de items
    lenght = len(items)

    # La memoria almacena los resultados de la recursion, para no exceder el numero de llamadas
    memory: dict[int, list[Item]] = {}

    def recursion(n):
        '''
        En este metodo siempre se retorna una lista con todas las condiciones 
        de forma que se generen los 0's que faltan para que el tamaño de 
        la lista devuelta sea el mismo que el de la lista de items para 
        poder recorrerlas en paralelo. Ej:

        memory[n] = [1, 0, 1]\n
        (Si la longitud debe ser de 5)\n
        res = [0, 0, 1, 0, 1]
        '''

        if n == 0:
            return [0]
        if n == 1:
            return [1]

        if n in memory:
            return memory[n]

        memory[n] = [n % 2] + recursion(math.floor(n / 2))

        return [0] * (lenght - len(memory[n])) + memory[n]

    def sum_items(conditions):
        '''
        Este metodo agrega a la variable de all_sums cada una de las sumas totales
        como clave y el contennido sera la lista que generó ese valor total. Ej:

        conditions = [1, 0, 0, 1, 0, 1]\n
        items = [a, b, c, d, e, f]

        total_value = a + d + f\n
        all_sums[total_value] = items
        '''
        
        selected_items = []
        total_value = 0
        total_weight = 0

        for condition, item in zip(conditions, items):
            if condition and total_weight + item.weight <= MAX_WEIGHT:
                selected_items.append(item)
                total_value += item.value
                total_weight += item.weight
            elif total_weight + item.weight > MAX_WEIGHT:
                # Si el peso excede el peso maximo entonces retorno 0 para que no se tome en cuenta
                total_value = 0
                break

        all_sums[total_value] = selected_items

    # Aqui se generan todas las formas posibles de combinar elementos en forma de condiciones 1's y 0's
    # 1 -> se va a sumar
    # 0 -> no se va a sumar
    condition_list: list[list[bool]] = [
        recursion(i) for i in range(2 ** lenght)
    ]

    # Se completa el diccionario de all_sums con todas las condiciones generadas
    for condition in condition_list:
        sum_items(condition)

    return all_sums[max(all_sums.keys())]
