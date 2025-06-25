from fastapi import FastAPI, HTTPException
from models import Task
import tasks as task_service
#lembrar de tentar usar try/catch

app = FastAPI()



@app.get("/tarefas")
def listar():
    return task_service.get_all_tasks()

@app.post("/tarefas")
def criar(task: Task):
    return task_service.create_task(task)

@app.get("/tarefas/{task_id}")
def obter(task_id: int):
    task = task_service.get_task(task_id)
    if task:
        return task
    raise HTTPException(status_code=404, detail="notfound")

@app.put("/tarefas/{task_id}")
def atualizar(task_id: int, task: Task):
    updated = task_service.update_task(task_id, task) #verifcar dps 
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="notfound")

@app.delete("/tarefas/{task_id}")
def deletar(task_id: int):
    return task_service.delete_task(task_id)
