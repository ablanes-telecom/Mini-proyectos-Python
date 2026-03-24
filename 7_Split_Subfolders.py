import os

def split(path,niveles):
    if niveles <= 0:
        return
    for i in range(0,2):
        nombre_subcarpeta = f"Nivel_{niveles}_Carpeta_{i+1}"
        nueva_ruta = os.path.join(path, nombre_subcarpeta)
        
        os.makedirs(nueva_ruta, exist_ok=True)
        
        # La función se llama a sí misma para bajar al siguiente nivel
        split(nueva_ruta, niveles - 1)

path=input('Path de la carpeta: ')
print(split(path,3))