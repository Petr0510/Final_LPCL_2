
import random
from ClsMijugador import MiJugador
from ClsMonstruo import Monstruo
from ClsMapa import Mapa
import cv2
import mediapipe as mp
import numpy as np
import verificarLado

def pedirN():
    n = input('Digite N, la cantidad de filas y columnas: ')
    print('Se hará una matriz de ' + n + 'Filas y columnas')
    n= int(n)
    return n

def main():
    
    # #Variable de la malla facial
    # mp_face_mesh= mp.solutions.face_mesh

    # face_mesh = mp_face_mesh.FaceMesh(
    #     min_detection_confidence=0.5,
    #     min_tracking_confidence=0.5)

    # #Abrir la cámara web
    # cap = cv2.VideoCapture(0)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH,260) 
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT,220)
# ● El mapa del juego estará representado por una matriz NxN
    n = pedirN()
    mapa = Mapa(n,n)
    mapa.crearMapa()

     # ● El jugador aparecerá en una posición aleatoria de la matriz con vida 10 e inventario vacío
    jugx = random.randint(0,n-1)
    jugy = random.randint(0,n-1)
    jugador = MiJugador(10,jugx,jugy,[])
    mapa.setCelda(jugx,jugy,"[P]")

    # ● Además, aparecerá un monstruo con vida 100 que se moverá de manera aleatoria y afectará al jugador, quitándole vida.
    Monx=random.randint(0,n-1)
    Mony=random.randint(0,n-1)

    #Poner al monstruo en una posicion aleatoria diferente al jugador
    while (Mony == jugy and Monx == jugx):
        Monx=random.randint(0,n-1)
        Mony=random.randint(0,n-1)
    monstruo = Monstruo(100,Monx,Mony)
    mapa.setCelda(Monx,Mony,"[M]")

    #iniciar el gameloop
    Gameloop(mapa,jugador,monstruo)
    
def Gameloop(mapa,jugador,monstruo):
    num_turnos =0
    while (jugador.estaVivo() and monstruo.estaVivo()):

        #Despues de 10 turnos volver a llenar los objetos
        if num_turnos == 10:
            mapa.llenarMapa()
            num_turnos=0
        
        print("Tu turno:")
        jugador.imprimirEstado()
        mapa.imprimir()
        Dec= int(input("\n 1. Mover"+
                "\n 2. Comer"+
                "\n 3. Recoger Arma"+
                "\n 4. Atacar\n"))
    
        mapa.imprimir()
        match Dec:
            case 1:
                #El juego se jugará por turnos donde el jugador podrá Moverse
                # (arriba, derecha, izquierda, abajo)
                # Opc= int(input("\n 1. Arriba"+
                  #              "\n 2. Abajo"+
                  #               "\n 3. Izquierda"+
                  #              "\n 4. Derecha\n")   )
                Opc = verificarLado.ppal() 
                
                jugador.Mover(Opc,mapa)
            case 2:
                #El juego se jugará por turnos donde el jugador podrá comer
                # (+10 de vida por cada comida, si hay una comida en mi posición)
                jugador.comer(mapa)
            case 3:
                #El juego se jugará por turnos donde el jugador podrá recoger arma 
                # (agrega el arma de esa posición si la hay al inventario, armas infinitas)
                jugador.AgregarArma(random.choice(["Espada","Baston","Arco","Daga","hacha"]),mapa)
            case 4:
                # El juego se jugará por turnos donde el jugador podrá atacar al monstruo 
                #  (-10 de vida al monstruo, ataca desde cualquier distancia, la ultima arma del inventario)
                jugador.atacar(monstruo)
                if not(monstruo.estaVivo()):
                    break
        
        print(jugador.getX(),jugador.getY())
        print(monstruo.getX(),monstruo.getY())
    
        if jugador.getX() == monstruo.getX() and jugador.getY() == monstruo.getY():
            monstruo.atacar(jugador)
            # ● El juego se acaba si el jugador o el monstruo tienen vida 0
            if not(jugador.estaVivo()):
                
                break
    
        mapa.imprimir()
        # ● El monstruo se moverá aleatoriamente y si cae en la celda
        #  del jugador, le quitará 25 de vida
        monstruo.mover(mapa,jugador)
        mapa.imprimir()
        
        if jugador.getX() == monstruo.getX() and jugador.getY() == monstruo.getY():
            monstruo.atacar(jugador)
             # ● El juego se acaba si el jugador o el monstruo tienen vida 0
            if not(jugador.estaVivo()):
                break
        num_turnos +=1


    if monstruo.estaVivo():
        print("Gana el monstruo")
    else:
        print("Gana el jugador")

# # ● Usted puede definir los detalles de cada una de las acciones de ambos personajes,
# # comidas y armas que usará en el juego
# # ● Toda la lógica del juego se hará vía consola pero los controles del juego se deben
# # controlar con movimientos faciales 😮, como por ejemplo: mover la cabeza a la
# # derecha o izquierda, abrir la boca, subir una ceja, etc.
#     # ○ Para esto, usará librerías completas de visión artificial que le ayudarán a
#     # interpretar los movimientos de la cara.
#     # ○ En esta práctica, entenderán los conceptos básicos de Face Landmark
#     # Detection y Head Position Estimation.

if __name__ == '__main__':
    main()