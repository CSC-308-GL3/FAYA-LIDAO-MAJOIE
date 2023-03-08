class Navire:

    def __init__(self, noNavire, nomNavire, libelleFret, qteFret):
        self.__noNavire = noNavire,
        self.__nomNavire = nomNavire,
        self.__libelleFret = libelleFret,
        self.__qteFret = qteFret

    ##Fonction obtenirQuantiteFret
    def obtenirQteFret(self):
        return self.__qteFret

    ##Fonction decharger
    def decharger(self, qte):
        self.__qteFret -= qte

    ##Fonction estDecharge
    def estDecharge(self):
        return self.__qteFret == 0
        

    
        