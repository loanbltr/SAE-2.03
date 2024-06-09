from django.shortcuts import render, HttpResponseRedirect
from .forms import JoueursForm
from . import models

# Create your views here.
def joueurs_index(request):
    liste = list(models.Joueurs.objects.all().order_by('nom'))
    return render(request, "joueurs/index.html", {"liste" : liste})

def joueurs_ajout(request):
    if request.method == "POST":
        form = JoueursForm(request)
        if form.is_valid():
            joueurs = form.save()
            return render(request, "joueurs/affiche.html", {"joueurs": joueurs})

        else:
            return render(request, "joueurs/ajout.html", {"form": form})
    else:
        form = JoueursForm()
        return render(request, "joueurs/ajout.html", {"form": form})


def joueurs_traitement(request):
    jform = JoueursForm(request.POST)
    if jform.is_valid():
        joueurs = jform.save()
        return HttpResponseRedirect("/index_joueurs/")
    else:
        return render(request, "joueurs/ajout.html", {"form": jform})

def joueurs_affiche(request, id):
    joueur = models.Joueurs.objects.get(pk=id)
    commentaires = models.Commentaires.objects.filter(joueurs=joueur)
    return render(request, "joueurs/affiche.html", {"joueur": joueur, "commentaires": commentaires})

def joueurs_update(request, id):
    liste = models.Joueurs.objects.get(pk=id)
    form = JoueursForm(liste.__dict__)
    return render(request, "joueurs/ajout.html", {"form":form, "id": id})

def joueurs_updatetraitement(request, id):
    jform = JoueursForm(request.POST)
    if jform.is_valid():
        joueurs = jform.save(commit = False)
        joueurs.id = id
        joueurs.save()
        return HttpResponseRedirect("/index_joueurs/")
    else:
        return render(request, "joueurs/ajout.html", {"form": jform, "id":id})

def joueurs_delete(request, id):
    joueurs = models.Joueurs.objects.get(pk=id)
    joueurs.delete()
    return HttpResponseRedirect("/index_joueurs/")