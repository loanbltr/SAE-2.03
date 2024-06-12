from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import JeuxForm
from .models import Jeux, Commentaires, Joueurs
from PIL import Image
from django.db.models import Avg
import os
from django.conf import settings
from . import models

# Create your views here.
def jeux_index(request):
    liste = list(Jeux.objects.all())
    return render(request, "jeux/index.html", {"liste" : liste})

def jeux_ajout(request):
    if request.method == "POST":
        form = JeuxForm(request.POST, request.FILES)
        if form.is_valid():
            jeux = form.save()
            jeux.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "jeux/ajout.html", {"form": form})
    else:
        form = JeuxForm()
        return render(request, "jeux/ajout.html", {"form": form})


def jeux_traitement(request):
    jform = JeuxForm(request.POST, request.FILES)
    if jform.is_valid():
        jeux = jform.save()

        if jeux.photo:
            resize_image(jeux.photo.path)

        return HttpResponseRedirect("/")
    else:
        return render(request, "jeux/ajout.html", {"form": jform})

def resize_image(image_path):
    with Image.open(image_path) as img:
        img = img.resize((50, 50), Image.LANCZOS)
        img.save(image_path)

from django.db.models import Avg

def jeux_affiche(request, id):
    jeux = get_object_or_404(Jeux, pk=id)
    liste = list(models.ListeJeuxJoueurs.objects.filter(jeux_id=id))
    listeCommentaires = Commentaires.objects.filter(jeux=jeux)
    nbCommentaires = listeCommentaires.count()

    commentaires_pro = listeCommentaires.filter(joueurs__type='professionnel')
    commentaires_particulier = listeCommentaires.filter(joueurs__type='particulier')

    nombre_joueurs = len(liste)

    averageRatingPro = commentaires_pro.aggregate(Avg('note'))['note__avg']
    averageRatingParticulier = commentaires_particulier.aggregate(Avg('note'))['note__avg']

    if averageRatingPro is None:
        averageRatingPro = "NN"
    if averageRatingParticulier is None:
        averageRatingParticulier = "NN"

    bestCommentaire = listeCommentaires.order_by('-note').first()
    pireCommentaire = listeCommentaires.order_by('note').first()

    return render(request, "jeux/affiche.html", {
        "jeux": jeux,
        "nbCommentaires": nbCommentaires,
        "averageRatingPro": averageRatingPro,
        "averageRatingParticulier": averageRatingParticulier,
        "bestCommentaire": bestCommentaire,
        "pireCommentaire": pireCommentaire,
        "listeCommentaires": listeCommentaires,
        "liste": liste,
        "nombre_joueurs": nombre_joueurs,
    })

def jeux_update(request, id):
    liste = Jeux.objects.get(pk=id)
    form = JeuxForm(instance=liste)
    return render(request, "jeux/ajout.html", {"form":form, "id": id})


def jeux_updatetraitement(request, id):
    jform = JeuxForm(request.POST, request.FILES)
    if jform.is_valid():
        jeux = jform.save(commit=False)
        jeux.id = id
        jeux.save()

        if jeux.photo:
            resize_image(jeux.photo.path)

        return HttpResponseRedirect("/")
    else:
        return render(request, "jeux/ajout.html", {"form": jform, "id": id})

def jeux_delete(request, id):
    jeux = Jeux.objects.get(pk=id)
    jeux.delete()
    return HttpResponseRedirect("/")