from django.shortcuts import render
from django.http import HttpResponse
from db import Film
from search import searchFilm

# обработчики запросов пути
def main(request):
    return render(request, "main.html")

def search(request):
    return render(request, "search.html")

def film(request, id):
    return render(request, "film.html", {"film": Film(id)})

def find(request):
    if "value" in request.GET:
        value = request.GET['value']
        films = searchFilm(value)
    else:
        films=""
    return HttpResponse(f"""{films}""")

# def index(request):
#     return render(request, "index.html")
