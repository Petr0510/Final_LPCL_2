from ClsPersonaje import Personaje

class MiJugador(Personaje):
    def __init__(self, vida, x, y, inventario ):
        super().__init__(vida, x, y)
        self.__inventario = inventario

    def imprimirEstado(self):
        print("Mi vida: "+str(self.getVida()))
        print("Mi Posición: ("+str(self.getX() ) +"," + str(self.getY() )+")")
        print("Mi inventario: "+str(self.__inventario))

    def comer(self,Mapa):
        if Mapa.getCelda(self.getX(),self.getY())=="[Po]":

            vid = self.getVida()
            vid+=10
            self.setVida(vid)
            
            Mapa.setCelda(self.getX(),self.getY(),"[P]")
            print("Has comido, tu vida ha aumentado 10 puntos ahora tu vida es: " + str(self.getVida()))
        elif Mapa.getCelda(self.getX(),self.getY())=="[PMo]":
            vid = self.getVida()
            vid+=10
            self.setVida(vid)
            Mapa.setCelda(self.getX(),self.getY(),"[PM]")
            print("Has comido, tu vida ha aumentado 10 puntos ahora tu vida es: " + str(self.getVida()))
        else:
            print("No hay comida en tu posición")
    
    def atacar(self,monstruo):
        if len(self.__inventario)!=0:
            monstruo.recibirDaño(10)
            print("Has causado 10 de daño al monstruo su vida es ahora" + str(monstruo.getVida()))
            self.__inventario.pop()
        else:
            print("No hay armas en tu inventario")
    
    def AgregarArma(self,Arma,Mapa):
        if Mapa.getCelda(self.getX(),self.getY()) =="[Pa]":
            self.__inventario.append(Arma)
            Mapa.setCelda(self.getX(),self.getY(),"[P]")
            print("Has recogido "+ Arma + " y ha sido agreada al inventario")
        elif Mapa.getCelda(self.getX(),self.getY()) =="[PMa]":
            self.__inventario.append(Arma)
            Mapa.setCelda(self.getX(),self.getY(),"[PM]")
            print("Has recogido "+ Arma + " y ha sido agreada al inventario")
        else:
            print("No hay arma que recoger")
    
    def Mover(self,opcion,Mapa):
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
                if Mapa.getColumnas()-1>=self.getX()+1:
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
                if Mapa.getFilas()-1>=self.getY()+1:
                    valor = self.getY()
                    valor+=1
                    self.setY(valor)
                else:
                    print("Movimiento invalido")
        if (xant!= self.getX() or yant != self.getY()):
            #se movió
            if Mapa.getCelda(xant, yant)=="[P]":
                Mapa.setCelda(xant, yant,"[ ]")
            elif Mapa.getCelda(xant, yant)  == "[PM]":
                Mapa.setCelda(xant, yant,"[M]")
            elif Mapa.getCelda(xant, yant)=="[Po]":
                Mapa.setCelda(xant, yant,"[o]")
            elif Mapa.getCelda(xant, yant)=="[Pa]":
                Mapa.setCelda(xant, yant,"[a]")
            elif Mapa.getCelda(xant, yant)=="[PMo]":
                Mapa.setCelda(xant, yant,"[Mo]")
            elif Mapa.getCelda(xant, yant)=="[PMa]":
                Mapa.setCelda(xant, yant,"[Ma]")

            if Mapa.getCelda(self.getX(), self.getY())=="[ ]":
                Mapa.setCelda(self.getX(),self.getY(),"[P]")
            elif Mapa.getCelda(self.getX(), self.getY())=="[M]":
                Mapa.setCelda(self.getX(),self.getY(),"[PM]")
            elif Mapa.getCelda(self.getX(), self.getY())=="[o]":
                Mapa.setCelda(self.getX(),self.getY(),"[Po]")
            elif Mapa.getCelda(self.getX(), self.getY())=="[a]":
                Mapa.setCelda(self.getX(),self.getY(),"[Pa]")
            elif Mapa.getCelda(self.getX(), self.getY())=="[Mo]":
                Mapa.setCelda(self.getX(),self.getY(),"[PMo]")
            elif Mapa.getCelda(self.getX(), self.getY())=="[Ma]":
                Mapa.setCelda(self.getX(),self.getY(),"[PMa]")
            
            
                

