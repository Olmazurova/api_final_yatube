# Yatube
Yatube — это платформа для блогов.

На этом блог-сервисе можно зарегистрироваться, создать, отредактировать или удалить собственный пост.
А также можно прокомментировать пост другого автора или подписаться на него.
Делитесь всем интересным из своей жизни, будьте в курсе событий других!

В проекте создано API на основе Django Rest Framework, через который можно взаимодействовать с платформой.

### Доступные ендпоинты:
- api/v1/jwt/create/ - получение токена по логину и паролю
- api/v1/jwt/refresh/ - обновление токена
- api/v1/jwt/verify/ - проверка токена
- api/v1/posts/ - список всех постов, либо создание поста
- api/v1/posts/{post_id}/ - просмотр, редактирование или удаление поста
- api/v1/groups/ - список всех групп
- api/v1/groups/{group_id}/ - информация о группе с соответствующим id
- api/v1/posts/{post_id}/comments/ - список всех комментариев поста или создание комментария к посту
- api/v1/posts/{post_id}/comments/{comment_id}/ - просмотр, редактирование или удаление комментария
- api/v1/follow/ - список подписок пользователя

### Как развернуть проект локально:

**1. Клонировать репозиторий и перейти в него в командной строке:**

`git clone https://github.com/Olmazurova/api_final_yatube.git`

**2. Cоздать и активировать виртуальное окружение:**

- На ОС Linux:

`python3 -m venv env`

`source env/bin/activate`

`python3 -m pip install --upgrade pip`

- На ОС Windows:

`python -m venv .venv`
  
`source .venv/Scripts/activate`

`python -m pip install --upgrade pip`

**3. Установить зависимости из файла requirements.txt:**

`pip install -r requirements.txt`

**4. Выполнить миграции:**

- На ОС Linux:

`python3 manage.py migrate`

- На ОС Windows:

`python manage.py migrate`

**5. Запустить проект:**

- На ОС Linux:

`python3 manage.py runserver`

- На ОС Windows:

`python manage.py runserver`


### Примеры запросов
- Создание публикации
`{
  "text": "Текст нового поста.",
  "image": "картинка",
  "group": 0
}`

- Добавление комментария к посту
`{
  "text": "Текст комментария к посту."
}`

- Подписаться на пользователя
`{
  "following": "username"
}`

- Получить токен
`{
  "username": "New_user",
  "password": "Change_me!"
}`



_____
Автор проекта: Ольга Мазурова

