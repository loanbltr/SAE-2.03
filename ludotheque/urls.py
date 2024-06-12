from django.urls import path
from . import views, views_joueurs, views_auteurs, views_categories, views_jeux, views_commentaires, views_listejeuxjoueurs


urlpatterns = [
    path('check_permissions/', views.check_permissions),

    path('', views.indexmain),
    path('index/', views.index),

    path('index_joueurs/', views_joueurs.joueurs_index),
    path('ajout_joueurs/', views_joueurs.joueurs_ajout),
    path('traitement_joueurs/', views_joueurs.joueurs_traitement),
    path('affiche_joueurs/<int:id>/', views_joueurs.joueurs_affiche),
    path('update_joueurs/<int:id>/', views_joueurs.joueurs_update),
    path('updatetraitement_joueurs/<int:id>/', views_joueurs.joueurs_updatetraitement),
    path('delete_joueurs/<int:id>/', views_joueurs.joueurs_delete),

    path('index_auteurs/', views_auteurs.auteurs_index),
    path('ajout_auteurs/', views_auteurs.auteurs_ajout),
    path('traitement_auteurs/', views_auteurs.auteurs_traitement),
    path('affiche_auteurs/<int:id>/', views_auteurs.auteurs_affiche),
    path('update_auteurs/<int:id>/', views_auteurs.auteurs_update),
    path('updatetraitement_auteurs/<int:id>/', views_auteurs.auteurs_updatetraitement),
    path('delete_auteurs/<int:id>/', views_auteurs.auteurs_delete),

    path('index_categories/', views_categories.categories_index),
    path('ajout_categories/', views_categories.categories_ajout),
    path('traitement_categories/', views_categories.categories_traitement),
    path('affiche_categories/<int:id>/', views_categories.categories_affiche),
    path('update_categories/<int:id>/', views_categories.categories_update),
    path('updatetraitement_categories/<int:id>/', views_categories.categories_updatetraitement),
    path('delete_categories/<int:id>/', views_categories.categories_delete),

    path('index_jeux/', views_jeux.jeux_index),
    path('ajout_jeux/', views_jeux.jeux_ajout),
    path('traitement_jeux/', views_jeux.jeux_traitement),
    path('affiche_jeux/<int:id>/', views_jeux.jeux_affiche, name='affiche_jeux'),
    path('update_jeux/<int:id>/', views_jeux.jeux_update),
    path('updatetraitement_jeux/<int:id>/', views_jeux.jeux_updatetraitement),
    path('delete_jeux/<int:id>/', views_jeux.jeux_delete),

    path('index_commentaires/', views_commentaires.commentaires_index),
    path('ajout_commentaires/', views_commentaires.commentaires_ajout),
    path('traitement_commentaires/', views_commentaires.commentaires_traitement),
    path('affiche_commentaires/<int:id>/', views_commentaires.commentaires_affiche),
    path('update_commentaires/<int:id>/', views_commentaires.commentaires_update),
    path('updatetraitement_commentaires/<int:id>/', views_commentaires.commentaires_updatetraitement),
    path('delete_commentaires/<int:id>/', views_commentaires.commentaires_delete),

    path('index_listejeuxjoueurs/', views_listejeuxjoueurs.listejeuxjoueurs_index),
    path('ajout_listejeuxjoueurs/<int:id>/', views_listejeuxjoueurs.listejeuxjoueurs_ajout),
    path('traitement_listejeuxjoueurs/<int:id>/', views_listejeuxjoueurs.listejeuxjoueurs_traitement),
    path('affiche_listejeuxjoueurs/<int:id>/', views_listejeuxjoueurs.listejeuxjoueurs_affiche),
    path('update_listejeuxjoueurs/<int:id>/', views_listejeuxjoueurs.listejeuxjoueurs_update),
    path('updatetraitement_listejeuxjoueurs/<int:id>/', views_listejeuxjoueurs.listejeuxjoueurs_updatetraitement),
    path('delete_listejeuxjoueurs/<int:id>/<int:jeux_id>/', views_listejeuxjoueurs.listejeuxjoueurs_delete),

    path('joueurs/export/<int:id>/', views_joueurs.export_orders),
    path('import_product/', views.import_product, name='import_product'),
    ]