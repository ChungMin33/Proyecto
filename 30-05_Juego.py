#-----------------bloque de inports------------------
from random import randint
#----------------------------------------------------

#-----------------bloque de funciones-----------------
carta_random = 0
def random_card():
    diamonts = ["DA","D2","D3","D4","D5","D6","D7","D8","D9","DT","DJ","DQ","DK"]
    cloves = ["CA","C2","C3","C4","C5","C6","C7","C8","C9","CT","CJ","CQ","CK"]
    hearts = ["HA","H2","H3","H4","H5","H6","H7","H8","H9","HT","HJ","HQ","HK"]
    spades = ["SA","S2","S3","S4","S5","S6","S7","S8","S9","ST","SJ","SQ","SK"]
    masos_total = [diamonts,cloves,hearts,spades]
    a = randint(0,3)
    b = randint(0,12)
    carta_random = masos_total[a][b]
    #valor de cartas
    numeros = ["2","3","4","5","6","7","8","9",]
    print(carta_random)
    for i in numeros:
        if i in carta_random:
            valor = int(i)

    letras = ["T","J","Q","K"]
    for i in letras:
        if i in carta_random:
            valor = 10

    if "A" in carta_random:
        valor = 1
    return carta_random, valor
#-----------------------------------------------------

#-----------------bloque de variables------------------
grupier = 0
carta_grupier = []

jugador = 0
carta_jugador = []
#------------------------------------------------------

#-----------------bloque de ejecucion-----------------
#paso 1, dar bienvenida y preguntar nombre

print("***Bienvenido a la partida de BlackJack***")
name = input("Ingrese su UserName\n")
print(f"Buena suerte {name}!")


#paso 2, se reparten 2 cartas a cada uno, con la segunda del grupier volteada
while len(carta_jugador) != 2:
    carta_random1, valor1 = random_card()
    carta_random2, valor2 = random_card()
    carta_grupier.append(carta_random1)
    grupier += valor1

    carta_jugador.append(carta_random2)
    jugador += valor2

print(f"Casa: {carta_grupier[0]}, [-]")
print(f"{name}: {carta_jugador}")
#--------------------------------------------------------------------


#paso 3, comienza el juego, abrimos un menu con las opciones que desea usar el jugador 
flag_opcion = False
while  not flag_opcion:
    print("---Que desea hacer?---")
    print("1.- Otra carta")
    print("2.- Quedarse")
    print("3.- Dividir")
    print("----------------------")

    #ingreso de la opcion, cuidando los errores
    try:
        opcion = int(input("Ingrese la opcion: "))
        if opcion < 1 or opcion > 3:
            raise ValueError
        
    except ValueError:
        print("----------------------------------------")
        print("Ingrese un numero dentro de las opciones")
        print("----------------------------------------")

    #primera opcion, añadirle una carta mas al jugador
    if opcion == 1:
        carta_random2, valor2 = random_card()
        carta_jugador.append(carta_random2)
        jugador += valor2
        print(carta_jugador)
        if jugador > 21:    #si la carta añadida, sumada a las cartas ya obtenidas, supera los 21 el jugador pierde
            print("Perdiste")
            flag_opcion = True

    #segunda opcion, quedarse con las cartas obtenidas(con o sin cartas adicionales obtenidas anteriormente)
    if opcion == 2:
        print(f"{name}: {carta_jugador}")

        #abrimos un ciclo para que el grupier pida cartas hasta ganarle al jugador o hasta que se pase de los 21
        flag_win = False
        while not flag_win:
            #se le añade una carta al grupier en caso de que tenga puntuacion menor a 17
            if grupier < 17:
                carta_random1, valor1 = random_card()
                carta_grupier.append(carta_random1)
                grupier += valor1
                print(f"Casa: {carta_grupier}")

            #si el grupier tiene puntuacion menor al jugador y menor a 21 pide otra carta 
            elif grupier < jugador and grupier < 21:
                carta_random1, valor1 = random_card()
                carta_grupier.append(carta_random1)
                grupier += valor1
                print(f"Casa: {carta_grupier}")

            #si la puntuacion del grupier es mayor a la del jugador y menor o igual a 21 el jugador pierde
            elif grupier > jugador and grupier <= 21:
                print(f"Casa: {carta_grupier}")
                print("Perdiste")
                flag_opcion = True
                flag_win = True

            #si el grupier tiene puntuacion mayor a 21 el jugador gana
            elif grupier > 21:
                print("----------------------")
                print(f"Casa: {carta_grupier}")
                print("Ganaste")
                flag_opcion = True
                flag_win = True

    #tercera opcion(en desarrollo), dividir las cartas obtenidas
    if opcion == 3:
        #solo se puede dividir si la mano tine 2 cartas
        if len(carta_jugador) != 2:
            print("solo puede dividir la mano con 2 cartas")
        
        #si tiene 2 cartas en la mano pasa a dividir
        elif len(carta_jugador) == 2:
            #creamos una nueva mano para el jugador y una nueva varible contadora para
            #el puntaje del jugador
            carta_jugador_2 = []
            jugador2 = 0
            #agregamos la carta a la nueva mano
            carta_jugador_2.append(carta_jugador[1])
            #eliminamos la carta de la mano n°1
            jugador -= valor2
            carta_jugador.pop(1)
            print(f"{name}\nMano N°1: {carta_jugador}\nMano N°2: {carta_jugador_2}")


        print("---Que desea hacer?---")
        print("1.- Usar Mano 1")
        print("2.- Usar Mano 2")
        print("----------------------")

        try:
            opcion2 = int(input("Ingrese la opcion: "))
            if opcion2 < 1 or opcion2 > 2:
                raise ValueError
            
        except ValueError:
            print("----------------------------------------")
            print("Ingrese un numero dentro de las opciones")
            print("----------------------------------------")
        if opcion2 == 1:
            #si desea usar la primera mano, se cierra el ciclo y se devuelve al inicio
            flag_win = False
        elif opcion2 == 2:
            flag_opcion2 = False
            while  not flag_opcion2:
                print("---Que desea hacer?---")
                print("1.- Otra carta")
                print("2.- Quedarse")
                print("----------------------")

                try:
                    opcion3 = int(input("Ingrese la opcion: "))
                    if opcion3 < 1 or opcion3 > 2:
                        raise ValueError
                    
                except ValueError:
                    print("----------------------------------------")
                    print("Ingrese un numero dentro de las opciones")
                    print("----------------------------------------")

                if opcion3 == 1:
                    carta_random3, valor3 = random_card()
                    carta_jugador_2.append(carta_random3)
                    jugador2 += valor3
                    print(carta_jugador_2)
                    if jugador2 > 21:
                        print("Perdiste")
                        flag_opcion2 = True

                if opcion3 == 2:
                    print(f"{name}\n Mano N°2 {carta_jugador_2}")
                    flag_win = False
                    while not flag_win:
                        if grupier < 17:
                            carta_random1, valor1 = random_card()
                            carta_grupier.append(carta_random1)
                            grupier += valor1
                            print(f"Casa: {carta_grupier}")

                        elif grupier > jugador and grupier <= 21:
                            print(f"Casa: {carta_grupier}")
                            print("Perdiste")
                            flag_opcion = True
                            flag_win = True

                        elif grupier < jugador and grupier < 21:
                            carta_random1, valor1 = random_card()
                            carta_grupier.append(carta_random1)
                            grupier += valor1
                            print(f"Casa: {carta_grupier}")


                        elif grupier > 21:
                            print("----------------------")
                            print(f"Casa: {carta_grupier}")
                            print("Ganaste")
                            flag_opcion = True
                            flag_win = True