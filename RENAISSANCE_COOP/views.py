# from email import message
from django.shortcuts import redirect, render
from RENAISSANCE_COOP.models import Produit, Comment
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

# sert a creer un commentaire
def comment(request):

    if request.method == "POST":


        comment = Comment()
        comment.description = request.POST["comment"]
        comment.save()

        return redirect("/")
    else:
        comments = Comment.objects.all()
        return render(request, "comment.html",{"comments": comments})

# pour acheter un produit
def achat(request):
    produit = Produit.objects.get(id=request.POST["id"])
    produit.delete()
    return render(request, "achat.html")

# montre le produit deja cliqué
def actif(request):
    produit = Produit.objects.get(id=request.POST["id"])
    return render(request, "actif.html",{"produit": produit})

# ce qu'on voit, tout les produits
def home(request):
    produits = Produit.objects.all()
    # return HttpResponse('<h1>Hello Kevin</h1>')
    return render(request, "home.html", {"produits": produits})

# rien, juste un test
def result(request):
    return render(request, "result.html")

# pour se connecter
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "mauvais mot de passe ou nom d'utilisateur")
            return redirect("login")

    else:
        return render(request, "login.html")

# pour s'enregistrer
def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("nom deja pris")
                messages.info(request, "Nom déjà pris")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                print("email deja pris")
                messages.info(request, "Email déjà pris")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                user.save()
                print("compte créé")
                return redirect("login")
        else:
            print("password pas correct")
            messages.info(request, "Password pas correct")
            return redirect("register")
        return redirect("/")

    else:
        return render(request, "register.html")

# pour se déconnecter
def logout(request):
    auth.logout(request)
    return redirect("/")

# sert a creer un produit
def create(request):

    if request.method == "POST":

        produits = Produit()
        produits.name = request.POST["nom"]
        produits.img = request.POST["image"]
        produits.desc = request.POST["description"]
        produits.price = request.POST["prix"]
        produits.user = request.POST["user"]

        produits.save()
        return redirect("/")

    else:
        return render(request, "create.html")
