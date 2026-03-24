import string
import collections
import os
import re

archivo= input('Archivo de texto dentro de esta carpeta: ')
path=os.path.abspath(archivo)
#os.chdir(path)
res={
    'Líneas_totales': '',
    'Palabras_totales':'',
    'Palabras_únicas':'',
    'Carácteres_especiales':''
}
try:
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read()
        res['Líneas_totales']=len(contenido.splitlines())
        palabras=re.findall(r'\w+',contenido.lower())
        res['Palabras_totales']=len(palabras)
        palabras_unicas=set(palabras)
        res['Palabras_únicas']=len(palabras_unicas)
        caracteres_especiales= [c for c in contenido if c in string.punctuation] #para todas las letras devuelvelas si forman parte de todos los caracteres especiales
        res['Carácteres_especiales']=len(caracteres_especiales)
except FileNotFoundError:
    print(f'Error: El archivo "{archivo}" no existe.')
except IOError:
    print(f'Error: "{archivo}" no pudo ser leído.')
except Exception as e:
    print(f'Ocurrió un error inesperado: {e}')

print(res)




