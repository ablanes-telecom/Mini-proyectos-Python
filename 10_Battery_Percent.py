import psutil
import time

def show_battery():
    try:
        while True:
            battery = psutil.sensors_battery()
            porcentaje = battery.percent
            esta_enchufado = battery.power_plugged
            if porcentaje<= 20: 
                print('Batería Crítica')
                time.sleep(10*60)
            elif porcentaje>=21 and porcentaje <=30: 
                print('Batería baja, considera conectar el cargador')
                time.sleep(10*60)
            elif esta_enchufado==True: print(f'Sistema cargando: {porcentaje}%')
            else: 
                print(f"Estado OK: {porcentaje}%")
                time.sleep(5*60)
    except Exception as e: 
        print(f'No he sido capaz de saber cuanta bateria tienes: {e}')

show_battery()
        



