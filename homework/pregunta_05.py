"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("./files/input/data.csv", "r") as file:
        data = file.readlines()

    values = {}
    for line in data:
        parts = line.split("\t")
        letter = parts[0]
        value = int(parts[1])
        if letter in values:
            values[letter].append(value)
        else:
            values[letter] = [value]

    result = [(letter, max(vals), min(vals)) for letter, vals in values.items()]
    return sorted(result)