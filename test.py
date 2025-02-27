f = open('technofilm/searcher/names.txt', 'r', encoding='utf-8')
for i,name in enumerate(f.readlines()):
    print(i,name[:-1])