try:
    menu=int(input('Indica con un 1 para convertir de decimal a binario y un 2 para binario a decimal: '))
    if menu < 1 or menu > 2:
        raise ValueError
    if menu==1:
        decimal=int(input('Dame un num decimal: '))
        resultado=' '+'0b'
        while decimal>0:
            residuo=decimal%2
            resultado=str(residuo)+resultado 
            decimal=decimal//2
        print(resultado)
    elif menu==2:
        binario=input('Dame un numero binario: ')
        binario = binario[::-1]
        resultado=int()
        if binario.strip('01') != "":
            raise ValueError
        for i in range(len(binario)):
            if binario[i]=='1': resultado=resultado+2**i
        print('El número decimal es: ',resultado)
except ValueError:
    print ("please choose a valid option")