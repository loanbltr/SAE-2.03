from django.shortcuts import render, HttpResponseRedirect
from .forms import JeuxForm
from . import models

# Create your views here.
def jeux_index(request):
    liste = list(models.Jeux.objects.all())
    return render(request, "jeux/index.html", {"liste" : liste})

def jeux_ajout(request):
    if request.method == "POST":
        form = JeuxForm(request)
        if form.is_valid():
            jeux = form.save()
            return render(request, "jeux/affiche.html", {"jeux": jeux})

        else:
            return render(request, "jeux/ajout.html", {"form": form})
    else:
        form = JeuxForm()
        return render(request, "jeux/ajout.html", {"form": form})


def jeux_traitement(request):
    jform = JeuxForm(request.POST)
    if jform.is_valid():
        jeux = jform.save()
        return HttpResponseRedirect("/ludotheque/index_jeux/")
    else:
        return render(request, "jeux/ajout.html", {"form": jform})

def jeux_affiche(request, id):
    jeux = models.Jeux.objects.get(pk=id)
    return render(request, "jeux/affiche.html", {"jeux": jeux})

def jeux_update(request, id):
    liste = models.Jeux.objects.get(pk=id)
    form = JeuxForm(liste.__dict__)
    return render(request, "jeux/ajout.html", {"form":form, "id": id})

def jeux_updatetraitement(request, id):
    jform = JeuxForm(request.POST)
    if jform.is_valid():
        jeux = jform.save(commit = False)
        jeux.id = id
        jeux.save()
        return HttpResponseRedirect("/ludotheque/index_jeux/")
    else:
        return render(request, "jeux/ajout.html", {"form": jform, "id":id})

def jeux_delete(request, id):
    jeux = models.Jeux.objects.get(pk=id)
    jeux.delete()
    return HttpResponseRedirect("/ludotheque/index_jeux/")