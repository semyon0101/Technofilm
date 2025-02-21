import csv

_films=[]
with open('filmdata.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        _films.append(row)

class Film(dict):
    def __init__(self, id):
        self.id = id
        self.poster = _films[self.id+1][0]
        self.name = _films[self.id+1][1]
        self.dateCreated = _films[self.id+1][2]
        self.genre =_films[self.id+1][3]
        self.description = _films[self.id+1][4]
        dict.__init__(self, id=self.id, poster = self.poster, name=self.name, dateCreated=self.dateCreated, genre=self.genre, description=self.description)

        