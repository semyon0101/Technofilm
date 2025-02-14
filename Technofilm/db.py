import csv
_films=[]
with open('films.csv') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
                _films.append(row)
    except:
        pass

class Film:
    def __init__(self, id):
        self.id = id
        self.find()

    
    def find(self):
        self.name = _films[self.id+1][1]
        self.image = _films[self.id+1][2]
        self.description =_films[self.id+1][3]
        self.creationYear = _films[self.id+1][4]