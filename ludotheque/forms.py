from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class CategoriesForm(ModelForm):
    class Meta:
        model = models.Categories
        fields = ('nom', 'desc')
        labels = {
            'nom': _('Nom'),
            'desc': _('Description'),
        }

class JeuxForm(ModelForm):
    class Meta:
        model = models.Jeux
        fields = ('titre', 'anneeSortie', 'photo', 'editeur', 'auteur', 'cat')
        labels = {
            'titre' : _('Titre'),
            'anneeSortie' : _('Année de Sortie'),
            'photo': _('Photo'),
            'editeur': _('Editeur'),
            'auteur': _('Auteur'),
            'cat': _('Catégorie'),
        }

class AuteursForm(ModelForm):
    class Meta:
        model = models.Auteurs
        fields = ('nom', 'prenom', 'age', 'photo')
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prénom'),
            'age': _('Age'),
            'photo': _('Photo'),
        }

class JoueursForm(ModelForm):
    class Meta:
        model = models.Joueurs
        fields = ('nom', 'prenom', 'mail', 'mdp', 'type')
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prénom'),
            'mail': _('Mail'),
            'mdp': _('Mot de passe'),
            'type': _('Type'),
        }

class CommentairesForm(ModelForm):
    class Meta:
        model = models.Commentaires
        fields = ('jeux', 'joueurs', 'note', 'commentaire', 'date')
        labels = {
            'jeux' : _('Jeux'),
            'joueurs' : _('Joueurs'),
            'note': _('Note'),
            'commentaire': _('Commentaire'),
            'date': _('Date'),
        }

class ListeJeuxJoueursForm(ModelForm):
    class Meta:
        model = models.ListeJeuxJoueurs
        fields = ('joueurs',)
        labels = {
            'joueurs' : _('Joueurs'),
        }