import random
class Mapa:
    def __init__(self,Filas,Columnas):
        self.__Filas = Filas
        self.__Columnas = Columnas
        self.__Celdas = []
    def getFilas(self):
        return self.__Filas
    
    def getColumnas(self):
        return self.__Columnas
    
    def getCelda(self,i,j):
        return self.__Celdas[i][j]
    
    def setCelda(self,i,j,Valor):
        self.__Celdas[i][j] = Valor
        
    def crearMapa(self):
        for i in range(self.__Filas):
            self.__Celdas.append([])
            for j in range(self.__Columnas):
                self.__Celdas[i].append("[ ]")
        self.llenarMapa()


    # ● En el mapa aparecerán comidas y armas que beneficiarán al jugador para sobrevivir

    def llenarMapa(self):
         for i in range(self.__Filas):
            for j in range(self.__Columnas):
                if self.__Celdas[i][j] == "[o]" or self.__Celdas[i][j] == "[a]" or self.__Celdas[i][j] == "[ ]":
                    y = random.randint(1,3)
                    match y:
                        case 1:
                            #vacío
                            self.__Celdas[i][j]="[ ]"
                        case 2:
                            #comida
                            self.__Celdas[i][j]="[o]"
                        case 3:
                            #arma
                            self.__Celdas[i][j]="[a]"
    def imprimir(self):
    
        x= ""
        for i in range(self.__Filas):
            for j in range(self.__Columnas):
                x =x + self.__Celdas[i][j] + " "
            x+="\n"
        print(x)

 
