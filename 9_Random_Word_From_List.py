import random
import sys


filename = input("Archivo: ")

try:
    with open(filename, 'r', encoding='utf-8') as f: # Usamos 'with' para que el archivo se cierre solo pase lo que pase
        lineas = f.readlines() # Lee todas las líneas a una lista
        
    if lineas:
        # random.choice elige un elemento de la lista directamente
        print(random.choice(lineas).strip()) # el strip elimina los espacios vacios
    else:
        print("El archivo está vacío.")

except FileNotFoundError:
    print("¡Error! El archivo no existe.")