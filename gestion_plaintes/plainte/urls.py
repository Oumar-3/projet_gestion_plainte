from django.urls import path
from	.views	import	*


urlpatterns = [
    path('', accueil, name='accueil'),
    path('index/', index, name='index'),
    path('inscription/', inscription, name='inscription'),
    path('login/', connexion, name='login'),
    path('logout/', deconnexion, name='logout'),
    path('liste_plainte/', liste_plainte, name='liste_plainte'),
    path('liste_plainte/ajouter/', ajouter_plainte, name='ajouter_plainte'),  
    path('liste_plainte/modifier/<int:id>/',modifier_plainte, name='modifier_plainte'),
    path('liste_plainte/supprimer/<int:id>/',supprimer_plainte, name='supprimer_plainte'),
]
