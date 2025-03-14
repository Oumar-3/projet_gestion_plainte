from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def _str_(self):
        return self.nom

class Plainte(models.Model):
    STATUTS = [
        ('En attente', 'En attente'),
        ('En cours', 'En cours'),
        ('Résolu', 'Résolu'),
    ]
    
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien avec l'utilisateur
    titre = models.CharField(max_length=255)  # Nouveau champ pour le titre
    description = models.TextField()
    categorie = models.CharField(max_length=100)  # Nouveau champ pour la catégorie
    statut = models.CharField(max_length=20, choices=STATUTS, default='En attente')  # Champ pour le statut
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plainte de {self.utilisateur.username} - {self.statut}"


class Reponse(models.Model):
    plainte = models.ForeignKey(Plainte, on_delete=models.CASCADE)
    message = models.TextField()
    date_reponse = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Réponse à {self.plainte.titre}"
