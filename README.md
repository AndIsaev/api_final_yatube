# api_final
Проект api final позволяет получить информацию в формате JSON 
Реализована аутентификация по JWT-токену

Документация  на локальной машине:
http://localhost:8000/redoc/

GET http://localhost:8000/posts/ - получение всех записей

POST http://localhost:8000/api/v1/token/ - передав поля username и password. API вернет JWT-токен
yamdb_final
Yamdb-app workflow

Учебный проект от Яндекс.Практикум, представляет собой DRF API приложение базы отзывов о фильмах, книгах и музыке с пройденым код ревью.

Стек технологий:
Python3
Django
Django REST Framework
Docker
Docker-compose
Build
docker-compose build.

Migrate databases
docker-compose run --rm web code/manage.py migrate.

Run
docker-compose up.

Подробная документация основана на Redoc и доступна по адресу: http://127.0.0.1:8020/redoc после запуска контейнера
