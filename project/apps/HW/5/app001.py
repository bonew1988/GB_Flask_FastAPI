# Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание. Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех задач.
# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
# — POST /tasks — добавляет новую задачу.
# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic.


from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Task(BaseModel):
    title: str
    description: str
    status: bool = False


tasks_db: List[Task] = []


@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    """Получение списка всех задач."""
    return tasks_db


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int = Path(..., title="Идентификатор задачи")):
    """Получение задачи с указанным идентификатором."""
    try:
        return tasks_db[task_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="Задача не найдена")


@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    """Добавление новой задачи."""
    tasks_db.append(task)
    return task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    """Обновление задачи с указанным идентификатором."""
    try:
        tasks_db[task_id - 1] = task
        return task
    except IndexError:
        raise HTTPException(status_code=404, detail="Задача не найдена")


@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    """Удаление задачи с указанным идентификатором."""
    try:
        return tasks_db.pop(task_id - 1)
    except IndexError:
        raise HTTPException(status_code=404, detail="Задача не найдена")
