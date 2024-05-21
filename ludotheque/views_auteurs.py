from django.shortcuts import render, HttpResponseRedirect
from .forms import AuteursForm
from . import models

# Create your views here.
def auteurs_index(request):
    liste = list(models.Auteurs.objects.all())
    return render(request, "auteurs/index.html", {"liste" : liste})

def auteurs_ajout(request):
    if request.method == "POST":
        form = AuteursForm(request)
        if form.is_valid():
            auteurs = form.save()
            return render(request, "auteurs/affiche.html", {"auteurs": auteurs})

        else:
            return render(request, "auteurs/ajout.html", {"form": form})
    else:
        form = AuteursForm()
        return render(request, "auteurs/ajout.html", {"form": form})


def auteurs_traitement(request):
    aform = AuteursForm(request.POST)
    if aform.is_valid():
        auteurs = aform.save()
        return HttpResponseRedirect("/ludotheque/index_auteurs/")
    else:
        return render(request, "auteurs/ajout.html", {"form": aform})

def auteurs_affiche(request, id):
    auteurs = models.Auteurs.objects.get(pk=id)
    return render(request, "auteurs/affiche.html", {"auteurs": auteurs})

def auteurs_update(request, id):
    liste = models.Auteurs.objects.get(pk=id)
    form = AuteursForm(liste.__dict__)
    return render(request, "auteurs/ajout.html", {"form":form, "id": id})

def auteurs_updatetraitement(request, id):
    aform = AuteursForm(request.POST)
    if aform.is_valid():
        auteurs = aform.save(commit = False)
        auteurs.id = id
        auteurs.save()
        return HttpResponseRedirect("/ludotheque/index_auteurs/")
    else:
        return render(request, "auteurs/ajout.html", {"form": aform, "id":id})

def auteurs_delete(request, id):
    auteurs = models.Auteurs.objects.get(pk=id)
    auteurs.delete()
    return HttpResponseRedirect("/ludotheque/index_auteurs/")