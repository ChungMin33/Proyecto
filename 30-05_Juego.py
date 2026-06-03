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
    if "A" in carta_random:
        valor = 1
    if "2" in carta_random:
        valor = 2
    elif "3" in carta_random:
        valor = 3
    elif "4" in carta_random:
        valor = 4
    elif "5" in carta_random:
        valor = 5
    elif "6" in carta_random:
        valor = 6
    elif "7" in carta_random:
        valor = 7
    elif "8" in carta_random:
        valor = 8
    elif "9" in carta_random:
        valor = 9
    elif "T" in carta_random:
        valor = 10
    elif "J" in carta_random:
        valor = 10
    elif "Q" in carta_random:
        valor = 10
    elif "K" in carta_random:
        valor = 10
    return carta_random, valor
#-----------------------------------------------------

#-----------------bloque de variables------------------
grupier = 0
carta_grupier = []

jugador = 0
carta_jugador = []
#------------------------------------------------------

#bloque de ejecucion
#paso 1, repartir cartas

print("***Bienvenido a la partida de BlackJack***")
name = input("Ingrese su UserName\n")
print(f"Buena suerte {name}!")


flag_game = False
while not flag_game:
    while len(carta_jugador) != 2:
        carta_random1, valor1 = random_card()
        carta_random2, valor2 = random_card()
        carta_grupier.append(carta_random1)
        grupier += valor1
    
        carta_jugador.append(carta_random2)
        jugador += valor2

    print(f"Casa: {carta_grupier[0]}, [-]")
    print(f"{name}: {carta_jugador}")
    
    flag_opcion = False
    while  not flag_opcion:
        print("---Que desea hacer?---")
        print("1.- Otra carta")
        print("2.- Quedarse")
        print("----------------------")

        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            carta_random2, valor2 = random_card()
            carta_jugador.append(carta_random2)
            jugador += valor2
            print(carta_jugador)
            if jugador > 21:
                flag_game = True
                flag_opcion = True
                print("Perdiste")

        elif opcion == 2:

            print(f"Casa: {carta_grupier}")
            print(f"{name}: {carta_jugador}")
            if valor1 < 17:
                carta_random1, valor1 = random_card()
                carta_grupier.append(carta_random1)
                grupier += valor1
                print(f"Casa: {carta_grupier}")
                opcion = 2
                if grupier > jugador and grupier <= 21:
                    print("Perdiste")
                    
                elif grupier < jugador and grupier < 21:
                        while grupier < jugador and grupier < 21:
                            carta_random1, valor1 = random_card()
                            carta_grupier.append(carta_random1)
                            grupier += valor1
                            print(f"Casa: {carta_grupier}")
                            if grupier >= jugador and grupier < 21:
                                print("Perdiste")
                                flag_game = True
                                flag_opcion = True
                            elif grupier > 21:
                                print("Ganaste")
                                flag_game = True
                                flag_opcion = True
                elif grupier > 21:
                    print("Ganaste")
                    flag_game = True
                    flag_opcion = True



