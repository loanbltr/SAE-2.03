from django.shortcuts import render, HttpResponseRedirect
from .forms import ListeJeuxJoueursForm
from . import models

# Create your views here.
def listejeuxjoueurs_index(request):
    liste = list(models.ListeJeuxJoueurs.objects.all())
    return render(request, "listejeuxjoueurs/index.html", {"liste" : liste})

def listejeuxjoueurs_ajout(request):
    if request.method == "POST":
        form = ListeJeuxJoueursForm(request)
        if form.is_valid():
            listejeuxjoueurs = form.save()
            return render(request, "listejeuxjoueurs/affiche.html", {"listejeuxjoueurs": listejeuxjoueurs})

        else:
            return render(request, "listejeuxjoueurs/ajout.html", {"form": form})
    else:
        form = ListeJeuxJoueursForm()
        return render(request, "listejeuxjoueurs/ajout.html", {"form": form})


def listejeuxjoueurs_traitement(request):
    ljjform = ListeJeuxJoueursForm(request.POST)
    if ljjform.is_valid():
        listejeuxjoueurs = ljjform.save()
        return HttpResponseRedirect("/ludotheque/index_listejeuxjoueurs/")
    else:
        return render(request, "listejeuxjoueurs/ajout.html", {"form": ljjform})

def listejeuxjoueurs_affiche(request):
    liste_jeux_joueurs = models.ListeJeuxJoueurs.objects.all()
    return render(request, 'listejeuxjoueurs/index.html', {'liste_jeux_joueurs': liste_jeux_joueurs})

def listejeuxjoueurs_update(request, id):
    liste = models.ListeJeuxJoueurs.objects.get(pk=id)
    form = ListeJeuxJoueursForm(liste.__dict__)
    return render(request, "listejeuxjoueurs/ajout.html", {"form":form, "id": id})

def listejeuxjoueurs_updatetraitement(request, id):
    ljjform = ListeJeuxJoueursForm(request.POST)
    if ljjform.is_valid():
        listejeuxjoueurs = ljjform.save(commit = False)
        listejeuxjoueurs.id = id
        listejeuxjoueurs.save()
        return HttpResponseRedirect("/ludotheque/index_listejeuxjoueurs/")
    else:
        return render(request, "listejeuxjoueurs/ajout.html", {"form": ljjform, "id":id})

def listejeuxjoueurs_delete(request, id):
    listejeuxjoueurs = models.ListeJeuxJoueurs.objects.get(pk=id)
    listejeuxjoueurs.delete()
    return HttpResponseRedirect("/ludotheque/index_listejeuxjoueurs/")