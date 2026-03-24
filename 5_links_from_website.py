from bs4 import BeautifulSoup
import requests as rq

url=input('Página web :')
if ("https" or "http") in url: #por si el enlace no incluye el protocolo en el input
    respuesta = rq.get(url)
else:
    respuesta = rq.get("https://" + url)

soup=BeautifulSoup(respuesta.text, 'html.parser')#respuesta.text es el archivo qu se genera con la linea anterior, el html puro
final=[]
for a in soup.find_all('a'):
    enlace=a.get('href')
    final.append(enlace)

print('Los enlaces son',final[:10])