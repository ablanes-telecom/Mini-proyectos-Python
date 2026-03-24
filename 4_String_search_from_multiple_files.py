
import os

text=input('El texto a reconocer: ')
estacarpeta=input('Path: ')


def get_files(path):
    os.chdir(path)
    files=os.listdir(path)
    for file_name in files:
        # 1. Verificamos que sea un archivo y no una subcarpeta
        if os.path.isfile(file_name):
            try:
                # 2. Abrimos el archivo y lo guardamos en 'f'
                with open(file_name, "r", encoding="utf-8") as f:
                    # 3. Leemos el contenido real del archivo
                    contenido = f.read()
                    
                    # 4. Buscamos el texto dentro del contenido
                    if text in contenido:
                        # Mostramos la ruta completa
                        print("Encontrado en:", os.path.abspath(file_name)) #convierte en una ruta completa
            except:
                # Esto ignora archivos que no se pueden leer (como imágenes o PDFs)
                continue
get_files(estacarpeta)