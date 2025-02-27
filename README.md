Чтобы заработал сервер нужно:
1. Утсановить файл 180.zip ( https://drive.google.com/file/d/1P6c8EEB95TSuEbuGgo_8cdZucAj9jvfK/view?usp=sharing )и установить его в папку technofilm/technofilm/searcher 
2. Открыть командную строку проекта и написать:
   cd Technofilm
   python manage.py runserver
3. Для нахождения ссылки на сайт посмотрите в ту самую командную строку. Будет написано что-то такое:
   Starting development server at http://127.0.0.1:8000/ - здесь и будет ссылка на открывшийся сайт

Примечание:
1. База фильмов - Technofilm/filmdata.csv
2. Скрипт для сбора фильмов - tensorflow-parser.zip
3. Алгоритм поиска представлен в функции search в Technofilm/searcher/test.py
4. веб сервис - Technofilm/
