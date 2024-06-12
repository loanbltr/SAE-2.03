from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, FileResponse
from .forms import JoueursForm, CommentairesForm
from . import models
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

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
    listejeux = list(models.ListeJeuxJoueurs.objects.filter(joueurs_id=id))
    commentaires = models.Commentaires.objects.filter(joueurs=joueur)
    return render(request, "joueurs/affiche.html", {"joueur": joueur, "commentaires": commentaires, 'listejeux': listejeux})

def joueurs_update(request, id):
    liste = models.Joueurs.objects.get(pk=id)
    form = JoueursForm(instance=liste)
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

def export_orders(request, id):
    joueurs_infos = models.Joueurs.objects.get(pk=id)
    commentaires = models.Commentaires.objects.filter(joueurs=joueurs_infos)
    liste_jeux = models.ListeJeuxJoueurs.objects.filter(joueurs=joueurs_infos)

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.setFont("Helvetica", 23)

    p.drawString(100, 750, f"Commentaires de {joueurs_infos.nom} {joueurs_infos.prenom}")

    p.setFont("Helvetica", 14)

    y_position = 700
    for commentaire in commentaires:
        jeu = commentaire.jeux
        note = commentaire.note
        commentaire_text = commentaire.commentaire

        p.drawString(100, y_position, f"Jeu: {jeu.titre}")
        p.drawString(200, y_position, f"Note: {note}")
        p.drawString(300, y_position, f"Commentaire: {commentaire_text}")

        y_position -= 60  # Augmenter cette valeur pour augmenter l'espacement entre les éléments

    p.setFont("Helvetica", 23)
    p.drawString(100, y_position, f"Liste des jeux de {joueurs_infos.nom} {joueurs_infos.prenom}")
    y_position -= 40
    p.setFont("Helvetica", 14)

    for jeu in liste_jeux:
        jeu = jeu.jeux

        p.drawString(100, y_position, f" • {jeu.titre}")

        y_position -= 20

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"{joueurs_infos.nom}{joueurs_infos.prenom}_{id}.pdf")
