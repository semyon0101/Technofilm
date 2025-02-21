from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from db import Film
from search import searchFilm
 
def main(request):
    return render(request, "main.html")

def search(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["value"]
            films = [Film(0)]
            return render(request, "search.html", {"form": userform, "films":films})
    return render(request, "search.html", {"form": userform, "films":[]})

def film(request, id):
    return render(request, "film.html", {"film": Film(id)})

def index(request):
    return render(request, "index.html")

def find(request):
    string = request.GET['string']
    films = searchFilm(string)
    return HttpResponse(f"""{films}""")