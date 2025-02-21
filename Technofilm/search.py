import json
from db import Film

def searchFilm(string):
    ids = [1,3,5,6]
    films = []
    for id in ids:
        films.append(Film(id))
    return json.dumps(films)