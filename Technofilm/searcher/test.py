import zipfile
import gensim
import tempfile
from natasha import Segmenter, NewsEmbedding, NewsMorphTagger, Doc
import db

segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)

def load_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip().split(',') for line in lines]

def get_word_with_pos(word):
    doc = Doc(word)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    pos = doc.tokens[0].pos
    return f"{word}_{pos}"

def find_lines_with_similar_words(word, tags, model, topn=10):
    word_with_pos = get_word_with_pos(word)

    if word_with_pos not in model:
        return []
        
    similar_words = [neighbor for neighbor, _ in model.most_similar(positive=[word_with_pos], topn=topn)]

    similar_words.append(word_with_pos)

    # print(similar_words)

    matching_lines = []
    for line in tags:
        for similar_word in similar_words:
            for object in line:
                if similar_word.split('_')[0] == object:
                    matching_lines.append(tags.index(line) + 1)

    return matching_lines



def search(string, maxLength=10):
    ids = []

    for i,film in enumerate(db._films): 
        if string.lower() in "".join(film[1:4]).lower():
            ids.append(i)

    if len(ids)>=maxLength:
        return ids[:maxLength]
    
    # Список слов для поиска
    word = string.lower()

    matching_lines = find_lines_with_similar_words(word, tags, model)

    matching_lines = list(set(matching_lines))
    for number in matching_lines:
        ids.append(number)
    return ids[:maxLength]

# Путь к zip-файлу
model_file = 'searcher/180.zip'

# Создаем временную директорию для извлечения файла модели
with tempfile.TemporaryDirectory() as temp_dir:
    with zipfile.ZipFile(model_file, 'r') as archive:
        archive.extract('model.bin', path=temp_dir)
        model_path = f"{temp_dir}/model.bin"

        # Загрузка модели с использованием gensim
        model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)

        # Путь к файлу с тегами
        tags_file_path = 'searcher/tags.txt'

        # Загрузка тегов из файла
        tags = load_tags(tags_file_path)
        names = open('searcher/names.txt', 'r', encoding='utf-8')