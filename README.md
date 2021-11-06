# programacion-ej2-"El-juego-de-adivinar"

Mi dirección de github para este repositorio es la siguiente: [GitHub](


Hemos resuelto un juego de adivinar con valores enteros entre 0 y 99.
El diagrama de flujo del codigo realizado, es el siguiente: 

No he conseguido que me funcione los if de si el intento elejido es demasiado pequeño o grande, me daba error en los símbolos (<>). Por eso he hecho otra versión en la que el if corresponde a si el intento = numero (generado aleatoriamente). 


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

    if intento == numero: 
        print ("¡Victoria!")
    else:
        print ("Fallaste")

        break ```
