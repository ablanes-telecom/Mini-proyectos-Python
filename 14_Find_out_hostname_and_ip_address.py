import socket
from urllib.parse import urlparse # Esto separa las partes de una UR

def get_hostname_IP():
    url_sucia=input('Copia la URL: ').strip() #para limpiar los espacios y obtener la URL
    if "://" in url_sucia:
        hostname = urlparse(url_sucia).netloc#Si el usuario pega https://es.wikipedia.org/wiki/Python, 
        #esta función "recorta" todo lo que sobra y se queda solo con el Network Location (netloc), es decir: es.wikipedia.org.
    else:
        hostname = url_sucia
    try:
        print (f'Hostname: {hostname}')
        print (f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print (f'Invalid Hostname, error raised is {error}')

get_hostname_IP()
#La IP que devuelve el código es el "número de teléfono" único que identifica al servidor en Internet. 
# Como los humanos preferimos recordar nombres (Hostname: google.com), el módulo socket consulta a una 
# agenda global llamada DNS para traducir ese nombre en la dirección numérica real (IP: 142.250.184.110) 
# que las máquinas necesitan para conectarse entre sí. 