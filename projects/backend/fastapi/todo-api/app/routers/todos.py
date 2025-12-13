from typing import List


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from .. import schemas, crud
from ..database import get_db


# APIRouter permite organizar as rotas em módulos separados.
router = APIRouter(
	prefix="/tasks",  # prefixo comum para todas as rotas: /tasks/...
	tags=["tasks"],   # grupo de tags para documentação
)


@router.get("/", response_model=List[schemas.Task])
def list_tasks(
    db: Session = Depends(get_db),  # injeta a sessão do banco via dependência
    skip: int = 0,                  # parâmetro de query: /tasks/?skip=0
    limit: int = 100,               # parâmetro de query: /tasks/?limit=100
):
    """
    Lista todas as tarefas com paginação simples.
    """
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks 


@router.get("/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    """
    Busca uma tarefa pelo ID.
    task_id vem do caminho da URL: /tasks/1, por exemplo.
    """
    task = crud.get_task(db, task_id)

    if not task:
        # Se a tarefa não existir, responde com erro HTTP 404.
        raise HTTPException(
    		status_code=status.HTTP_404_NOT_FOUND,
    		detail="Task not found",
    	)    	
    return task


@router.post(
	"/",
	response_model=schemas.Task,
	status_code=status.HTTP_201_CREATED,
)
def create_task(task_in: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova tarefa.
    task_in é lido automaticamente do corpo (JSON) da requisição.
    """
    task = crud.create_task(db, task_in)
    return task 


@router.put("/{task_id}", response_model=schemas.Task)
def update_task(
	task_in: int, 
	updates: schemas.TaskUpdate,    # dados que queremos atualizar
	db: Session = Depends(get_db),
):
    """
    Atualiza uma tarefa existente.
    """
    # Primeiro, busca a tarefa no banco
    task = crud.get_task(db, task_id)

    if not task:
        # Se não existir, retorna erro 404
    	raise HTTPException(
    		status_code=status.HTTP_404_NOT_FOUND,
    		detail="Task not found",
    	) 
    # Atualiza a tarefa com os dados recebidos
    task = crud.update_task(db, task, updates)
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Deleta uma tarefa pelo ID.
    """
    task = crud.get_task(db, task_id)

    if not task:
        # Se não existir, retorna erro 404
    	raise HTTPException(
    		status_code=status.HTTP_404_NOT_FOUND,
    		detail="Task not found",
    	) 
    # Remove a tarefa do banco
    crud.delete_task(db, task)
    # 204 No Content → sem corpo na resposta
    return
