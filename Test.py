import datetime

from Classes import Employe, Grade, Intervention, Contrat, Client

date_today = datetime.datetime.now()

grade = Grade('Expert', 'Grade Expert', 1000)

date_embauche = datetime.datetime(2015, 1, 17).date()

employe = Employe(1, 'FAYA', grade,  date_embauche)

client = Client(1, 'LANGUIE Mazamesso', 'Avedji Limousine', '75000', 'Lomé Togo', 100)

date_intervention = datetime.datetime(2023, 3, 1).date()

intervention1 = Intervention(1,  date_intervention, 2, 3.5, employe)

contrat = Contrat(1, date_embauche, client, 500.000)

contrat.setIntervention([intervention1])

ecart = contrat.ecart()

print("l' Ecart pour le contrat N {} est de: {} euros".format(contrat.numero, ecart))
