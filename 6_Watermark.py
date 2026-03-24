from PIL import Image
import os

imagen=input('Nombre de la imagen: ')
imagen=Image.open(imagen).convert('RGBA') #para que las dos tengan el mismo color y que se incluya la transparencia

capa_transparente=Image.new('RGBA',imagen.size,(0,0,0,0))
marca= input ('Marca: ')
marca= Image.open(marca).convert('RGBA')
peque=marca.resize((int((marca.size[0])/13),int((marca.size[1])/13)))
r, g, b, a = peque.split()
a = a.point(lambda p: p * 0.8) # 0.3 es el nivel de transparencia (30%)
peque = Image.merge('RGBA', (r, g, b, a))
capa_transparente.paste(peque,(int((imagen.width - peque.width) // 2),int((imagen.height - peque.height) // 2)),peque)
print(peque.size,imagen.size)
final=Image.alpha_composite(imagen,capa_transparente)
final.show()


        

