from django.shortcuts import render, HttpResponseRedirect
from .forms import CommentairesForm
from . import models

# Create your views here.
def commentaires_index(request):
    liste = list(models.Commentaires.objects.all())
    return render(request, "commentaires/index.html", {"liste" : liste})

def commentaires_ajout(request):
    if request.method == "POST":
        form = CommentairesForm(request)
        if form.is_valid():
            commentaires = form.save()
            return render(request, "commentaires/affiche.html", {"commentaires": commentaires})

        else:
            return render(request, "commentaires/ajout.html", {"form": form})
    else:
        form = CommentairesForm()
        return render(request, "commentaires/ajout.html", {"form": form})


def commentaires_traitement(request):
    cform = CommentairesForm(request.POST)
    if cform.is_valid():
        commentaires = cform.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "commentaires/ajout.html", {"form": cform})

def commentaires_affiche(request, id):
    commentaires = models.Commentaires.objects.get(pk=id)
    return render(request, "commentaires/affiche.html", {"commentaires": commentaires})

def commentaires_update(request, id):
    liste = models.Commentaires.objects.get(pk=id)
    form = CommentairesForm(instance=liste)
    return render(request, "commentaires/ajout.html", {"form":form, "id": id})

def commentaires_updatetraitement(request, id):
    cform = CommentairesForm(request.POST)
    if cform.is_valid():
        commentaires = cform.save(commit = False)
        commentaires.id = id
        commentaires.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "commentaires/ajout.html", {"form": cform, "id":id})

def commentaires_delete(request, id):
    commentaires = models.Commentaires.objects.get(pk=id)
    commentaires.delete()
    return HttpResponseRedirect("/")