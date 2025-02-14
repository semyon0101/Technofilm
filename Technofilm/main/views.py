from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from db import Film
 
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

