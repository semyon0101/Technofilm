import csv
import json
import re

#считываю файл
_films=[]
with open('filmdata.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        _films.append(row)

# класс фильм
class Film(dict):
    def __init__(self, id):
        self.id = id
        self.poster = _films[self.id+1][0]
        self.name = _films[self.id+1][1]
        self.dateCreated = _films[self.id+1][2]
        self.genres = list(json.loads(_films[self.id+1][3].replace('\'', '\"')))

        #распологаю в порядке убывания описания
        st=_films[self.id+1][4]
        st=st.replace('\'', '\"')
        st=st.replace('\\n','\n')
        st=st.replace('\\r',"\r")
        st=st.replace('\\t','\t')
        st = re.sub(r'(?![\w ,.\'\"\[\]\n\t\r])',r'',st)

        descriptions = st[2:-2].split("\", \"")
        if len(descriptions)!=2:
            print(self.id)

        
        if len(descriptions[0])>len(descriptions[1]):
            self.descriptions=[descriptions[0], descriptions[1]]
        else:
            self.descriptions=[descriptions[1], descriptions[0]]

        #это для json
        dict.__init__(self, id=self.id, poster = self.poster, name=self.name, dateCreated=self.dateCreated, genres=self.genres, descriptions=self.descriptions)

        