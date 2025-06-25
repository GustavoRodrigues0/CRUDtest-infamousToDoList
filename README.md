# API de Tarefas com FastAPI

## endpoints

- `GET /tarefas` — lista todas as tarefas
- `POST /tarefas` — cria uma nova
- `GET /tarefas/{id}` — retorna uma tarefa específica
- `PUT /tarefas/{id}` — atualiza
- `DELETE /tarefas/{id}` — deleta

## run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
