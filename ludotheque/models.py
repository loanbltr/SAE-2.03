from django.db import models

class Categories(models.Model):
    nom = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

    def dico(self):
        return {'nom': self.nom, 'desc':self.desc}

class Joueurs(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    mdp = models.CharField(max_length=100)
    TYPE_CHOICES = (
        ('professionnel', 'Professionnel'),
        ('particulier', 'Particulier'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        chaine = f"{self.nom} {self.prenom} "
        return chaine

    def dico(self):
        return {'nom': self.nom, 'prenom':self.prenom, 'mail':self.mail, 'mdp':self.mdp, 'type':self.type}

class Jeux(models.Model):
    titre = models.CharField(max_length=100)
    anneeSortie = models.IntegerField()
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    editeur = models.CharField(max_length=100)
    auteur = models.ForeignKey("Auteurs", on_delete=models.CASCADE, default=None)
    cat = models.ForeignKey("Categories", on_delete=models.CASCADE, default=None)
    joueurs = models.ManyToManyField(Joueurs, through='ListeJeuxJoueurs')

    def __str__(self):
        chaine = f" {self.titre} "
        return chaine

    def dico(self):
        return {'titre': self.titre, 'anneeSortie':self.anneeSortie, 'photo':self.photo, 'editeur':self.editeur, 'auteur':self.auteur, 'cat':self.cat}

class Auteurs(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        chaine = f"{self.nom} {self.prenom}"
        return chaine

    def dico(self):
        return {'nom': self.nom, 'prenom':self.prenom, 'age':self.age, 'photo':self.photo}

class Commentaires(models.Model):
    jeux = models.ForeignKey("Jeux", on_delete=models.CASCADE, default=None)
    joueurs = models.ForeignKey("Joueurs", on_delete=models.CASCADE, default=None)
    note = models.FloatField(max_length=3)
    commentaire = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=False)

    def __str__(self):
        chaine = f"Commentaire du joueur {self.joueurs} sur le jeu {self.jeux}"
        return chaine

    def dico(self):
        return {'jeux': self.jeux, 'joueurs':self.joueurs, 'note':self.note, 'commentaire':self.commentaire, 'date':self.date}

class ListeJeuxJoueurs(models.Model):
    jeux = models.ForeignKey("Jeux", on_delete=models.CASCADE, null=True)
    joueurs = models.ForeignKey("Joueurs", on_delete=models.CASCADE, null=True)
    def __str__(self):
        chaine = f"Voici la liste des jeux du joueur {self.joueurs} : {self.jeux}."
        return chaine

    def dico(self):
        return {'jeux': self.jeux, 'joueurs':self.joueurs}