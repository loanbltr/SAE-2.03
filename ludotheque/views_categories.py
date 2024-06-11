from django.shortcuts import render, HttpResponseRedirect
from .forms import CategoriesForm
from . import models

# Create your views here.
def categories_index(request):
    liste = list(models.Categories.objects.all())
    return render(request, "categories/index.html", {"liste" : liste})

def categories_ajout(request):
    if request.method == "POST":
        form = CategoriesForm(request)
        if form.is_valid():
            categories = form.save()
            return render(request, "categories/affiche.html", {"categories": categories})

        else:
            return render(request, "categories/ajout.html", {"form": form})
    else:
        form = CategoriesForm()
        return render(request, "categories/ajout.html", {"form": form})


def categories_traitement(request):
    cform = CategoriesForm(request.POST)
    if cform.is_valid():
        categories = cform.save()
        return HttpResponseRedirect("/index_categories/")
    else:
        return render(request, "categories/ajout.html", {"form": cform})

def categories_affiche(request, id):
    categories = models.Categories.objects.get(pk=id)
    return render(request, "categories/affiche.html", {"categories": categories})

def categories_update(request, id):
    liste = models.Categories.objects.get(pk=id)
    form = CategoriesForm(liste.__dict__)
    return render(request, "categories/ajout.html", {"form":form, "id": id})

def categories_updatetraitement(request, id):
    cform = CategoriesForm(request.POST)
    if cform.is_valid():
        categories = cform.save(commit = False)
        categories.id = id
        categories.save()
        return HttpResponseRedirect("/index_categories/")
    else:
        return render(request, "categories/ajout.html", {"form": cform, "id":id})

def categories_delete(request, id):
    categories = models.Categories.objects.get(pk=id)
    categories.delete()
    return HttpResponseRedirect("/index_categories/")