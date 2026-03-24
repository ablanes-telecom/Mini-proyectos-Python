import subprocess # Permite ejecutar comandos del sistema (terminal)
import re

# 1. Obtener la lista de redes guardadas (en la interfaz Wi-Fi, usualmente en0)
try:
    # Este comando de Mac lista todas las redes Wi-Fi a las que te has conectado.
    data = subprocess.check_output(["networksetup", "-listpreferredwirelessnetworks", "en0"]).decode("utf-8").split("\n")
    # Limpia los datos: salta la primera línea (que es un título) y quita espacios en blanco.
    profiles = [line.strip() for line in data[1:] if line.strip()]
except:
    #Si hay un error se crea una lista vacía
    profiles = []
# Imprime el encabezado de una tabla con formato: 30 espacios para el nombre | Contraseña
print("{:<30}|  {:<}".format("Red Wi-Fi", "Contraseña"))
print("-" * 50)# Dibuja una línea separadora

for ssid in profiles:
    # 2. Consultar el Llavero del sistema para esa red específica
    try:
        # El comando 'security' busca la contraseña en el llavero
        # -D "AirPort network password": Indica que buscamos una contraseña de Wi-Fi.
        # -ga "{ssid}": Busca el nombre de la red específica y pide mostrar la clave (-g).
        cmd = f'security find-generic-password -D "AirPort network password" -ga "{ssid}"'
        # Ejecuta el comando. 
        # NOTA: En este punto, macOS lanzará una ventana pidiendo usuario/contraseña de administrador.
        results = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        # Por seguridad, el comando 'security' envía la contraseña al flujo de error (stderr)
        # en lugar del flujo normal (stdout). Por eso leemos 'results.stderr'.
        output = results.stderr
        # Usamos Regex para buscar el patrón: password: "LA_CONTRASEÑA"
        password_match = re.search(r'password: "(.*)"', output)
        # Si encuentra la contraseña, la guarda; si no, deja el campo vacío.
        password = password_match.group(1) if password_match else ""
        # Imprime el nombre de la red y su contraseña alineados.
        print("{:<30}|  {:<}".format(ssid, password))
    except Exception:
        # Si algo falla (por ejemplo, si cancelas la ventana de permiso), muestra un error.
        print("{:<30}|  {:<}".format(ssid, "Error/No encontrada"))