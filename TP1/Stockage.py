class Stockage:
    
    def __init__(self, capaMax, capaDispo = -1):
        self.__capaMax = capaMax
        if capaDispo == -1 :
            self.__capaDispo = capaMax
        else:
            self.__capaDispo = capaDispo

    def obtenirCapaDispo(self):
        return self.__capaDispo

    def stocker(self, qte):
        self.__capaDispo -= qte

    def estVide(self):
        return self.__capaDispo == self.__capaMax

    def estRemplie(self):
        return self.__capaDispo == 0
