import json

if __name__=='__main__': #esto hace que si lo importamos a otro archivo esto no se ejucte directamente
    try:
        with open('input.json', 'r') as f:
            data = json.loads(f.read())
        output = ','.join([*data[0]])#[*data[0]] saca las llaves (nombres de columnas) del primer objeto. .join las une con comas para crear la primera línea del CSV.
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'#Añade una nueva línea (\n) y pega los valores de nombre, edad y año de nacimiento separados por comas.
        with open('output.csv','w') as f:
            f.write(output)

    except Exception as ex:
        print(f'Error: {str(ex)}')

#este codigo solo nos sirve para el archivo input, no para cualquiera.
