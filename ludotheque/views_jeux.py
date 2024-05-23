from django.shortcuts import render, HttpResponseRedirect
from .forms import JeuxForm
from . import models
from PIL import Image
import os
from django.conf import settings

# Create your views here.
def jeux_index(request):
    liste = list(models.Jeux.objects.all())
    return render(request, "jeux/index.html", {"liste" : liste})

def jeux_ajout(request):
    if request.method == "POST":
        form = JeuxForm(request.POST, request.FILES)
        if form.is_valid():
            jeux = form.save()
            jeux.save()
            return render(request, "jeux/index.html", {"jeux": jeux})

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

        return HttpResponseRedirect("/ludotheque/index_jeux/")
    else:
        return render(request, "jeux/ajout.html", {"form": jform})


def resize_image(image_path):
    with Image.open(image_path) as img:
        img = img.resize((50, 50), Image.LANCZOS)
        img.save(image_path)

def jeux_affiche(request, id):
    jeux = models.Jeux.objects.get(pk=id)
    return render(request, "jeux/affiche.html", {"jeux": jeux})

def jeux_update(request, id):
    liste = models.Jeux.objects.get(pk=id)
    form = JeuxForm(liste.__dict__)
    return render(request, "jeux/ajout.html", {"form":form, "id": id})


def jeux_updatetraitement(request, id):
    jform = JeuxForm(request.POST, request.FILES)
    if jform.is_valid():
        jeux = jform.save(commit=False)
        jeux.id = id
        jeux.save()

        if jeux.photo:
            resize_image(jeux.photo.path)

        return HttpResponseRedirect("/ludotheque/index_jeux/")
    else:
        return render(request, "jeux/ajout.html", {"form": jform, "id": id})

def jeux_delete(request, id):
    jeux = models.Jeux.objects.get(pk=id)
    jeux.delete()
    return HttpResponseRedirect("/ludotheque/index_jeux/")