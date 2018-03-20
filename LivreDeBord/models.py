from django.db import models
from datetime import date

class Evenement(models.Model):
    HIST = 'H'
    DEPENSE = 'D'
    RLV_EAU = 'W'
    RLV_ELEC = 'E'
    AUTRE = 'X'
    ENUM_CLASSE = (
        (HIST,'Histoire'),
        (DEPENSE,'Dépense'),
        (RLV_EAU,'Relevé Eau'),
        (RLV_ELEC,'Relevé électricité'),
        (AUTRE,'Autres')
    )
    libelle = models.CharField(max_length=100)
    date_event = models.DateField('Date', default=date.today)
    classe = models.CharField(max_length=1,choices=ENUM_CLASSE)
    
    def __str__(self):
        return self.classe+'-'+self.date_event.strftime('%x')
    
class Histoire(models.Model):
    lien_event = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.lien_event
    
class Depense(models.Model):
    ACHAT = 'A'
    DMNGT = 'D'
    EAU = 'W'
    ELEC = 'E'
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
        return self.type+'>'+self.lien_event
    
class ReleveEau(models.Model):
    lien_event = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    compteur = models.DecimalField('Index compteur',max_digits=5,decimal_places=1)
    
    def __str__(self):
        return 'R'+'>'+self.lien_event
    
class ReleveElec(models.Model):
    lien_event = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    heures_pleines = models.PositiveIntegerField('Heures Pleines')
    heures_creuses = models.PositiveIntegerField('Heures Creuses')
    
    def __str__(self):
        return 'R'+'>'+self.lien_event
    
    
    