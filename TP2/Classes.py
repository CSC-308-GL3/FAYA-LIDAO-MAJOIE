import datetime

class Grade:
    def __init__(self, code, libelle, taux):
        self.code = code
        self.libelle = libelle
        self.taux = taux

    def getCode(self):
        return self.code

    def getLibelle(self):
        return self.libelle

    def tauxHoraire(self):
        return self.taux

class Employe:
    def __init__(self, numero, nom, qualification, dateEmbauche):
        self.numero = numero
        self.nom = nom
        self.qualification = qualification
        self.dateEmbauche = dateEmbauche

    def coutHoraire(self):
        anciennete = self.getAncienete(self.dateEmbauche)
        taux = self.qualification.tauxHoraire()
        if anciennete < 5:
            return taux
        elif anciennete >= 5 and anciennete < 10:
            return (taux * 5)/100
        elif anciennete >= 11 and anciennete < 15:
            return (taux * 8)/100
        elif anciennete >15:
            return (taux * 12)/100
        else:
            return taux

    def getNumero(self):
        return self.numero

    def getNom(self):
        return self.nom

    def getQualification(self):
        return self.qualification

    def getDateEmbauche(self):
        return self.dateEmbauche

    def getAncienete(self, date):
        aujourdhui = datetime.datetime.now().date()
        annees = aujourdhui.year - date.year
        return annees

class Client:
    def __init__(self, numero, nom, adresse, codePostal, ville, nbKm):
        self.numero = numero
        self.nom = nom
        self.adresse = adresse
        self.codePostal = codePostal
        self.ville = ville
        self.nbKm = nbKm

    def distance(self):
        return self.nbKm

class Intervention:
    def __init__(self, numero, date, duree, tarifKm, technicien):
        self.numero = numero
        self.date = date
        self.duree = duree
        self.tarifKm = tarifKm
        self.technicien = technicien

    def affiche(self):
        print("Intervention n°", self.numero)
        print("Date :", self.date)
        print("Durée :", self.duree)
        print("Tarif kilométrique :", self.tarifKm)
        print("Technicien :", self.technicien.getNom())

    def fraisKm(self, dist):
        return self.tarifKm * dist

    def fraisMo(self):
        return self.technicien.coutHoraire() * self.duree

class Contrat:
    def __init__(self, numero, date, client, montantContrat):
        self.numero = numero
        self.date = date
        self.client = client
        self.montantContrat = montantContrat
        self.interventions = []
        self.nbIntervention = 0

    def montant(self):
        return self.montantContrat

    def setIntervention(self,interventions):
        self.interventions=interventions

    def ecart(self):
        coutTotal = 0
        for intervention in self.interventions:
            coutTotal += intervention.fraisKm(self.client.distance()) + intervention.fraisMo()
        return self.montantContrat - coutTotal
