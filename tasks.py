from typing import List
from models import Task

tasks: List[Task] = []

def get_all_tasks():
    return tasks

def create_task(task: Task):
    tasks.append(task)
    return task

def get_task(task_id: int):
    return next((t for t in tasks if t.id == task_id), None)

def update_task(task_id: int, updated_task: Task):
    for i, t in enumerate(tasks):
        if t.id == task_id:
            tasks[i] = updated_task
            return updated_task
    return None

def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
    return {"mensagem": "Tarefa deletada"}
