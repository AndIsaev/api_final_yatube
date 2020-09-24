# api_final
Проект api final позволяет получить информацию в формате JSON 
Реализована аутентификация по JWT-токену, поиск по полю "group"

Документация  на локальной машине:
http://localhost:8000/redoc/

GET http://localhost:8000/posts/ - получение всех записей

POST http://localhost:8000/api/v1/token/ - передав поля username и password. API вернет JWT-токен
