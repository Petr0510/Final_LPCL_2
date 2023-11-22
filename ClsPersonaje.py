class Personaje:
    def __init__(self,vida,x,y):
        self.__vida = vida
        self.__x=x
        self.__y=y

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getVida(self):
        return self.__vida
    
    def setX(self, x):
        self.__x=x

    def setY(self, y):
        self.__y=y

    def setVida(self, vida):
        self.__vida=vida
        
    
    def estaVivo(self):
        return self.__vida>0
    
    def recibirDaño(self,danio):
        self.__vida -=danio
        if self.__vida<0:
            self.__vida = 0
