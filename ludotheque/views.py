from django.shortcuts import render, HttpResponseRedirect
from .forms import JeuxForm
from . import models
import os
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
import csv
from django.utils.datastructures import MultiValueDictKeyError

def index(request):
    return render(request, 'index.html')

def indexmain(request):
    liste = list(models.Jeux.objects.all())
    return render(request, "main.html", {"liste": liste})

def check_permissions(request):
    media_root = settings.MEDIA_ROOT
    try:
        test_file_path = os.path.join(media_root, 'test.txt')
        with open(test_file_path, 'w') as test_file:
            test_file.write('test')
        os.remove(test_file_path)
        return HttpResponse('Permissions are OK')
    except Exception as e:
        return HttpResponse(f'Error: {e}')

def import_product(request):
    if request.method == 'POST':
        try:
            myfile = request.FILES['myfile']
        except MultiValueDictKeyError:
            messages.error(request, "Submit a CSV File please")
            return HttpResponseRedirect("/")

        decoded_file = myfile.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        required_fields = ['titre', 'anneeSortie', 'editeur', 'auteur', 'cat']

        for row in reader:
            missing_fields = [field for field in required_fields if field not in row]
            if missing_fields:
                messages.error(request,
                               f"Le fichier CSV ne contient pas toutes les colonnes nécessaires. Manquantes: {', '.join(missing_fields)}")
                return HttpResponseRedirect("/")

            # Process the author field
            auteur_instance = None
            if row['auteur']:
                auteur_nom, auteur_prenom = row['auteur'].split()
                auteur_instance, created = models.Auteurs.objects.get_or_create(
                    nom=auteur_nom,
                    prenom=auteur_prenom,
                    defaults={'age': 'Unknown'}
                )
            else:
                default_author, created = models.Auteurs.objects.get_or_create(
                    nom="Default",
                    prenom="Author",
                    defaults={'age': 'Unknown'}
                )
                auteur_instance = default_author

            # Validate category ID
            try:
                cat_instance = models.Categories.objects.get(id=row['cat'])
            except models.Categories.DoesNotExist:
                messages.error(request, f"Category with ID {row['cat']} does not exist.")
                return HttpResponseRedirect("/")

            # Create the game instance
            try:
                models.Jeux.objects.create(
                    titre=row['titre'],
                    anneeSortie=row['anneeSortie'],
                    editeur=row['editeur'],
                    auteur=auteur_instance,
                    cat=cat_instance,
                )
            except (ValueError, models.Jeux.DoesNotExist) as e:
                messages.error(request, f"Erreur d'importation: {e}")
                return HttpResponseRedirect("/")

        messages.success(request, "Les jeux ont été importés avec succès.")
        return HttpResponseRedirect("/")
    else:
        messages.error(request, "Erreur lors de l'importation. Veuillez réessayer.")
        return HttpResponseRedirect("/")
