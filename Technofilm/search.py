import json
from db import Film
from searcher.test import search
#функция для поиска фильмов. Принимает значение string- текста для поиска и возвращает json файл с фильмами
def searchFilm(string):
    print(string)
    ids = search(string)
    films = []
    for id in ids:
        print(id)
        films.append(Film(id))
    return json.dumps(films)