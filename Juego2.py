#importar biblotecas
import time
import random
import os



#inicio de juego/seleccion de fichas
def inicio_juego():
    print("****bienvenido****")
    time.sleep(1)
    while True:
        ficha = input("seleccione fichas: X / 0\n")
        ficha = ficha.upper()
        if ficha=="X":
            humano="X"
            ordenador="0"
            break
        elif ficha=="0":
            humano="0"
            ordenador="0"
            break
        else:
            print("Por favor, introduce una ficha posible. ")
    return(humano,ordenador)






#creaccion de tablero
def tablero():
    print("TRES EN RAYA / TIC TAC TOE")
    print()
    print("        |       |           ")
    print("1  {}    |2  {}   |3         ".format(matriz[0],matriz[1],matriz[2]))
    print("        |       |           ")
    print("-------------------------")
    print("        |       |           ")
    print("4   {}   |5  {}   |6         ".format(matriz[3],matriz[4],matriz[5]))                        
    print("        |       |           ")
    print("-------------------------")
    print("        |       |           ")
    print("7  {}    |8  {}   |9         ".format(matriz[6],matriz[7],matriz[8]))
    print("        |       |           ")


#definir finales de partidas
def empate(matriz):
    empate=True
    i=0
    while(empate==True and i<9):
        if matriz[i]==" ":
            empate=False
        i=i+1
    return empate

def victoria(matriz): 
    if (matriz[0]==matriz[1]==matriz[2]!=" " or matriz[3]==matriz[4]==matriz[5]!=" "or matriz[6]==matriz[7]==matriz[8]!=" "
        or matriz[0]==matriz[3]==matriz[6]!=" " or matriz[1]==matriz[4]==matriz[7]!=" " or matriz[2]==matriz[5]==matriz[8]!=" " or
        matriz[0]==matriz[4]==matriz[8]!=" " or matriz[2]==matriz[4]==matriz[6]!=" "):
        return True
    else:
        return False



#movimientos
def movimiento_jugador():
    while True:
        posiciones=[1,2,3,4,5,6,7,8,9]
        casilla=int(input("Seleccione casilla: "))
        if casilla not in posiciones:
            print("casillas no disponible")

        else:
            if matriz[casilla-1]==" ":
                matriz[casilla-1]==humano
                break
            else:
                print("Casilla no disponible")
def movimiento_ordenador():
    posiciones=[0,1,2,3,4,5,6,7,8]
    casilla=9
    parar=False

    for i in posiciones:
        copia=list(matriz)
        if copia[i]==" ":
            copia[i]=ordenador
            if victoria(copia)==True:
                casilla=i
    if casilla==9:
        for j in posiciones:
            if copia[j]==" ":
                copia[j]=humano
            if victoria(copia)==True:
                casilla=j

    if casilla==9:
        while(not parar):
            casilla=random.randint(0,8)
            if matriz[casilla]==" ":
                parar=True
    matriz[casilla]=ordenador

#desarrollo de partida

while True:

    matriz=[" "]*9
    os.system("cls") #limpiara la pantalla al comienzo de cada partida 
    humano,ordenador=inicio_juego()
    partida=True
    ganador=0

    while partida:
        ganador=ganador+1
        os.system("cls")
        tablero()

        if victoria(matriz):
            if ganador%2==0:
                print("**Gana el jugador**")
                print("**Fin del juego**")
                print("\nReiniciando...")
                time.sleep(5)
                partida=False
            else:
                print("**Gana el ordenador**")
                print("**Fin del juego**")
                print("\nReiniciando...")
                time.sleep(5)
                partida=False
        elif empate(matriz):
            print("**Empate")
            print("**Fin del juego**")
            print("\nReiniciando...")
            time.sleep(5)
            partida=False

        elif ganador%2==0:
            print("El ordenador esta pensando")
            time.sleep(2)
            movimiento_ordenador()

        else:
            movimiento_jugador()
            