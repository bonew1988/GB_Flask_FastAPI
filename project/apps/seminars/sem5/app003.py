# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя
# (методы POST, PUT, DELETE).
# Реализуйте валидацию данных запроса и ответа.

from fastapi import FastAPI

from .pydantic_models import User


app = FastAPI()
users: list[User] = []


@app.get('/')
async def index():
    return users


@app.post('/users/')
async def create_user(user: User):
    users.append(user)
    return user


@app.put('/users/{user_id}')
async def update_user(user_id: int, new_user: User):
    filtered_users = [user for user in users if user.id == user_id]
    if not filtered_users:
        return {'updated': False}

    user = filtered_users[0]

    user.name = new_user.name
    user.email = new_user.email
    user.password = new_user.password

    return {'updated': True, 'user': new_user}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    filtered_users = [user for user in users if user.id == user_id]
    if not filtered_users:
        return {'deleted': False}

    user = filtered_users[0]

    users.remove(user)

    return {'deleted': True, 'user': user}
