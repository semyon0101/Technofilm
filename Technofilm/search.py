import json
from db import Film
import random
#функция для поиска фильмов. Принимает значение string- текста для поиска и возвращает json файл с фильмами
def searchFilm(string):
    print(string)
    ids = []
    for i in range(random.randint(0,30)):
        ids.append(random.randint(0,5000))
    films = []
    for id in ids:
        films.append(Film(id))
    return json.dumps(films)