from django.shortcuts import render, HttpResponseRedirect
from .forms import AuteursForm
from . import models
from PIL import Image
from django.db.models import Avg

# Create your views here.
def auteurs_index(request):
    liste = list(models.Auteurs.objects.all())
    return render(request, "auteurs/index.html", {"liste" : liste})

def auteurs_ajout(request):
    if request.method == "POST":
        form = AuteursForm(request.POST, request.FILES)
        if form.is_valid():
            auteurs = form.save()
            auteurs.save()
            return render(request, "auteurs/affiche.html", {"auteurs": auteurs})

        else:
            return render(request, "auteurs/ajout.html", {"form": form})
    else:
        form = AuteursForm()
        return render(request, "auteurs/ajout.html", {"form": form})


def auteurs_traitement(request):
    aform = AuteursForm(request.POST, request.FILES)
    if aform.is_valid():
        auteurs = aform.save()
        if auteurs.photo:
            resize_image(auteurs.photo.path)

        return HttpResponseRedirect("/index_auteurs/")
    else:
        return render(request, "auteurs/ajout.html", {"form": aform})

def resize_image(image_path):
    with Image.open(image_path) as img:
        img = img.resize((50, 50), Image.LANCZOS)
        img.save(image_path)

def auteurs_affiche(request, id):
    auteurs = models.Auteurs.objects.get(pk=id)
    return render(request, "auteurs/affiche.html", {"auteurs": auteurs})

def auteurs_update(request, id):
    liste = models.Auteurs.objects.get(pk=id)
    form = AuteursForm(instance=liste)
    return render(request, "auteurs/ajout.html", {"form":form, "id": id})

def auteurs_updatetraitement(request, id):
    aform = AuteursForm(request.POST, request.FILES)
    if aform.is_valid():
        auteurs = aform.save(commit = False)
        auteurs.id = id
        auteurs.save()
        return HttpResponseRedirect("/index_auteurs/")
    else:
        return render(request, "auteurs/ajout.html", {"form": aform, "id":id})

def auteurs_delete(request, id):
    auteurs = models.Auteurs.objects.get(pk=id)
    auteurs.delete()
    return HttpResponseRedirect("/index_auteurs/")