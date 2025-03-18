from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Plainte, Categorie
from .forms import PlainteForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


def accueil(request):
    return render(request, 'plainte/accueil.html')

def index(request):
    return render(request, 'plainte/index.html')

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('liste_plainte')
    else:
        form = UserCreationForm()
    return render(request, 'plainte/inscription.html', {'form': form})


def connexion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('liste_plainte')  # Redirection après connexion
    else:
        form = AuthenticationForm()
    return render(request, 'plainte/login.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('accueil')  # Redirection après déconnexion


# Lire toutes les plaintes
def liste_plainte(request):
    plainte= Plainte.objects.all()
    return render(request, 'plainte/liste_plainte.html', {'plaintes': plainte})

# Créer une plainte
@login_required
def ajouter_plainte(request):
    if request.method == "POST":
        form = PlainteForm(request.POST)
        if form.is_valid():
            plainte = form.save(commit=False)  # Ne pas enregistrer immédiatement
            plainte.utilisateur = request.user  # Assigner l'utilisateur connecté
            plainte.save()  # Maintenant on sauvegarde ✅
            return redirect('liste_plainte')
    else:
        form = PlainteForm()
    return render(request, 'plainte/ajouter_plainte.html', {'form': form})

@login_required
def modifier_plainte(request, id):
    plainte = get_object_or_404(Plainte, id=id)
    if request.method == "POST":
        form = PlainteForm(request.POST, instance=plainte)
        if form.is_valid():
            form.save()
            return redirect('liste_plainte')  # Redirige vers la liste des plaintes
    else:
        form = PlainteForm(instance=plainte)
    
    return render(request, 'plainte/modifier_plainte.html', {'form': form})


# Supprimer une plainte
def supprimer_plainte(request, id):
    plainte = get_object_or_404(Plainte, id=id)
    if request.method == "POST":
        plainte.delete()
        return redirect('liste_plainte')
    return render(request, 'plainte/supprimer_plainte.html', {'plainte': plainte})

