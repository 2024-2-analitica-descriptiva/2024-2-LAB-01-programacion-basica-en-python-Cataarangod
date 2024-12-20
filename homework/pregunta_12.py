"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", "r") as file:
        data = file.read().splitlines()
    values = {}
    for row in data:
        parts = row.split("\t")
        for i in parts[4].split(","):
            if parts[0] not in values:
                values[parts[0]] = int(i.split(":")[1])
            else:
                values[parts[0]] += int(i.split(":")[1])
                
    return dict(sorted(values.items()))
print(pregunta_12())