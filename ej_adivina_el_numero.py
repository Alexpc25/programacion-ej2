import random 
numero = random.randint (0,99)


print ("Intente adivinar el numero")

while True:

    while True:
        intento = input ("Introduzca un numero entre el 0 y el 99 incluidos ")

        try: 
            initento = int(intento)
        except: 
            pass
        else: 
            if 0 <= numero <= 99:

                break

    if intento < numero: 
        print ("Demasiado pequeño")
    elif intento > numero: 
        print ("Demasiado Grande")
    else: 
        print ("¡Victoria!")

        break



