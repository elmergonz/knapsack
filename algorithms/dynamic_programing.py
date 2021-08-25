from constants import MAX_WEIGHT
from models.item import Item
import math

def dp_algorithm(items: list) -> list:
    '''
    Este algoritmo usa el metodo de fuerza bruta usando
    una memoria dinamica para optimizar el resultado
    '''

    all_sums: dict[float, list[Item]] = {}

    positions = len(items)
    memory: dict[int, list[Item]] = {}

    def recursion(n):
        if n == 0:
            return [0]
        if n == 1:
            return [1]

        if n in memory:
            return memory[n]

        memory[n] = [n % 2] + recursion(math.floor(n / 2))

        return [0] * (positions - len(memory[n])) + memory[n][::-1]

    def sum_items(conditions):
        selected_items = []
        total_value = 0.0
        total_weight = 0.0

        for condition, item in zip(conditions, items):
            if condition and total_weight + item.weight <= MAX_WEIGHT:
                selected_items.append(item)
                total_value += item.value
                total_weight += item.weight
            elif total_weight + item.weight > MAX_WEIGHT:
                # Si el peso excede el peso maximo entonces retorno 0 para que no se tome en cuenta
                total_value = 0.0
                break

        all_sums[total_value] = selected_items

    condition_list: list[list[bool]] = [recursion(i) for i in range(2 ** positions)]

    for condition in condition_list:
        sum_items(condition)

    return all_sums[max(all_sums.keys())]
