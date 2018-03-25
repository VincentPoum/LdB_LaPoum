from django.db import models
from datetime import date

class Evenement(models.Model):
    libelle = models.CharField(max_length=100)
    date_event = models.DateField('Date', default=date.today)
        
    def __str__(self):
        return self.date_event.strftime('%Y/%m/%d')
    def str_frise(self):
        return '"year":"'+self.date_event.strftime('%Y')+'","month":"'+self.date_event.strftime('%m')+'","day":"'+self.date_event.strftime('%d')+'"'
    
class Histoire(models.Model):
    lien_event = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return 'H>'+self.lien_event.__str__()
    
class Depense(models.Model):
    ACHAT = 'A'
    DMNGT = 'D'
    EAU = 'W'
    ELEC = 'Z'
    ENTRETIEN = 'E'
    TRAVX = 'T'
    FOURN = 'F'
    ENUM_TYPE_DEPENSE = (
        (ACHAT,'Achat'),
        (DMNGT,'Déménagement'),
        (EAU,'Facture eau'),
        (ELEC,'Facture électricité'),
        (ENTRETIEN,'Entretien'),
        (TRAVX,'Travaux'),
        (FOURN,'Fournitures')
    )
    lien_event = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    type = models.CharField('Type',max_length=1,choices=ENUM_TYPE_DEPENSE)
    somme = models.DecimalField('Montant',max_digits=8,decimal_places=2)
    notes = models.TextField()
    
    def __str__(self):
        return self.type+'>'+self.lien_event.__str__()
    
class ReleveEau(models.Model):
    lien_event = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    compteur = models.DecimalField('Index compteur',max_digits=5,decimal_places=1)
    
    def __str__(self):
        return 'R>'+self.lien_event.__str__()
    
class ReleveElec(models.Model):
    lien_event = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    heures_pleines = models.PositiveIntegerField('Heures Pleines')
    heures_creuses = models.PositiveIntegerField('Heures Creuses')
    
    def __str__(self):
        return 'R>'+self.lien_event.__str__()
    
    
    