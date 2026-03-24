import os
import shutil
import sys



def organizacion(path,num):
    # 1. Validar y cambiar de directorio
    if not os.path.isdir(path):
        print('Dirección no válida')
        return
    os.chdir(path)
    files = os.listdir('.') # Listamos lo que hay aquí
    num = int(num)
    splited = [files[i : i + num] for i in range(0, len(files), num)]
    for idx, trozo in enumerate(splited): #idx se queda con el 0 1 ... y el trozo con la sublista
        nombre_carpeta = f'Carpeta_{idx}'
        if not os.path.exists(nombre_carpeta):
            os.mkdir(nombre_carpeta)
        for archivo in trozo:
            # Movemos cada archivo individualmente a la carpeta
            try:
                shutil.move(archivo, nombre_carpeta)
            except Exception as e:
                print(f"No se pudo mover {archivo}: {e}")

path=input('Ruta de la carpeta: ')
max_archivos= input('Num max de archivos permitidos: ')
organizacion(path,max_archivos)






