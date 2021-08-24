from constants import MAX_WEIGHT
from models.item import Item

# Todos los algoritmos retornaran una lista de items

def h1_menor_peso(items: list) -> list:
    '''
    Esta heuristica va almacenando los items priorizando los que
    tienen menor peso hasta llenar el peso maximo
    '''

    sorted_items: list[Item] = sorted(items, key=lambda i: i.weight)

    result = []
    sum = 0

    for item in sorted_items:
        if sum + item.weight > MAX_WEIGHT:
            break

        sum += item.weight
        result.append(item)

    return result

def h2_mayor_valor(items: list) -> list:
    '''
    Esta heuristica va almacenando los items priorizando los que
    tienen mayor valor hasta llenar el peso maximo
    '''
    
    sorted_items: list[Item] = sorted(items, key=lambda i: i.value, reverse=True)

    result = []
    sum = 0

    for item in sorted_items:
        if sum + item.weight > MAX_WEIGHT:
            break

        sum += item.weight
        result.append(item)

    return result

def h3_mayor_cociente(items: list) -> list:
    '''
    Esta heuristica va almacenando los items priorizando los que
    tienen una mayor relacion valor/peso
    hasta llenar el peso maximo
    '''

    cocientes = [(item.value / item.weight, item) for item in items]
    sorted_items = sorted(cocientes, key=lambda i: i[0], reverse=True)

    result = []
    sum = 0

    for cociente, item in sorted_items:
        if sum + item.weight > MAX_WEIGHT:
            break

        sum += item.weight
        result.append(item)

    return result
