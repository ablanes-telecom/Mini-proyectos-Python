import os 
import shutil

# Configuración de rutas
home = os.path.expanduser("~")
downloads_path = os.path.join(home, "Downloads")
os.chdir(downloads_path)

# Lista de archivos actual
files = os.listdir(downloads_path)

# Carpeta principal de destino
base_dest = os.path.join(downloads_path, "download-sorting")
os.makedirs(base_dest, exist_ok=True)

extensions = {
    'images': [".jpg", ".png", ".jpeg", ".gif"],
    'videos': [".mp4", ".mkv"], 
    'musics': ['.mp3', '.wav', '.m4a'], 
    'zip': [".zip", ".tgz", ".rar", ".tar"], 
    'documents': [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"], 
    'setup': [".msi", ".exe"], 
    'programs': [".py", ".c", ".cpp", ".php", ".C", ".CPP"], 
    'design': [".xd", ".psd"]
}

def sorting(file):
    for key in extensions: #bucle por las keys de extensions
        for ext in extensions[key]: #bucle por los valores de las keys de extensions
            # Usamos lower() por si la extensión está en mayúsculas (.JPG)
            if file.lower().endswith(ext): 
                return key
    return None

for file in files:
    #Ignorar la carpeta de destino y archivos ocultos de Mac (que empiezan por un .)
    if file == "download-sorting" or file.startswith('.'):
        continue

    # Saltamos directorios para no intentar mover carpetas (solo archivos)
    if not os.path.isfile(file):
        continue

    category = sorting(file)
    dist = category if category else "others" #valor_si_verdadero if condicion else valor_si_falso
    
    # Creamos la subcarpeta de destino (ej: images) si no existe
    final_target_dir = os.path.join(base_dest, dist)
    os.makedirs(final_target_dir, exist_ok=True)

    try:
        # Movimiento seguro usando rutas completas
        shutil.move(file, os.path.join(final_target_dir, file))
        print(f"Organizado: {file} -> {dist}")
    except:
        print(f"Error: {file} ya existe en el destino o está abierto.")

print("\n--- ¡Proceso de limpieza terminado! ---")