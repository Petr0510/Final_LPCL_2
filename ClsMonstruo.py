from ClsPersonaje import Personaje
import random

class Monstruo(Personaje):
    def __init__(self, vida, x, y):
        super().__init__(vida, x, y)
        
    def atacar(self,Jugador):
        Jugador.recibirDaño(25)
        print("Daño a jugador por 25 nueva vida Jugador: " + str(Jugador.getVida()))

    def mover(self,Mapa,Jugador):
        opcion = random.randint(1,4)
        xant = self.getX()
        yant = self.getY()

        match opcion:
            case 1: #Arriba
                if self.getX()-1>=0:
                    valor = self.getX()
                    valor-=1
                    self.setX(valor)
                else:
                    print("Movimiento invalido")
            case 2: #Abajo
                if Mapa.getFilas()-1>=self.getX()+1:
                    valor = self.getX()
                    valor+=1
                    self.setX(valor)
                else:
                    print("Movimiento invalido")
            case 3: #Izquierda
                if self.getY()-1>=0:
                    valor = self.getY()
                    valor-=1
                    self.setY(valor)
                else:
                    print("Movimiento invalido")
            case 4: #Derecha
                if Mapa.getColumnas()-1>=self.getY()+1:
                    valor = self.getY()
                    valor+=1
                    self.setY(valor)
                else:
                    print("Movimiento invalido")
        if (xant!= self.getX() or yant != self.getY()):
            #se movió
            if Mapa.getCelda(xant, yant)=="[M]":
                Mapa.setCelda(xant, yant,"[ ]")
            elif Mapa.getCelda(xant, yant)  == "[PM]":
                # self.atacar(Jugador)
                Mapa.setCelda(xant, yant,"[P]")
            elif Mapa.getCelda(xant, yant)=="[Mo]":
                Mapa.setCelda(xant, yant,"[o]")
            elif Mapa.getCelda(xant, yant)=="[Ma]":
                Mapa.setCelda(xant, yant,"[a]")
            elif Mapa.getCelda(xant, yant)=="[PMo]":
                # self.atacar(Jugador)
                Mapa.setCelda(xant, yant,"[Po]")
            elif Mapa.getCelda(xant, yant)=="[PMa]":
                # self.atacar(Jugador)
                Mapa.setCelda(xant, yant,"[Pa]")

            if Mapa.getCelda(self.getX(), self.getY())=="[ ]":
                Mapa.setCelda(self.getX(),self.getY(),"[M]")
            elif Mapa.getCelda(self.getX(), self.getY())=="[P]":
                Mapa.setCelda(self.getX(),self.getY(),"[PM]")
                # self.atacar(Jugador)
            elif Mapa.getCelda(self.getX(), self.getY())=="[o]":
                Mapa.setCelda(self.getX(),self.getY(),"[Mo]")
            elif Mapa.getCelda(self.getX(), self.getY())=="[a]":
                Mapa.setCelda(self.getX(),self.getY(),"[Ma]")
            elif Mapa.getCelda(self.getX(), self.getY())=="[Po]":
                # self.atacar(Jugador)
                Mapa.setCelda(self.getX(),self.getY(),"[PMo]")
            elif Mapa.getCelda(self.getX(), self.getY())=="[Pa]":
                # self.atacar(Jugador)
                Mapa.setCelda(self.getX(),self.getY(),"[PMa]")
