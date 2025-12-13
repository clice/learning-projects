from sqlalchemy.orm import Session 


from . import models, schemas


def get_task(db: Session, task_id: int):
	"""
    Busca uma tarefa específica pelo ID.
    Retorna o objeto Task ou None se não existir.
    """
	return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
	"""
    Retorna uma lista de tarefas, com suporte a paginação simples.
    skip: quantos registros pular
    limit: máximo de registros retornados
    """
	return db.query(models.Task).offset(skip).limit(limit).all()


def create_task(db: Session, task: schemas.TaskCreate):
	"""
    Cria uma nova tarefa no banco a partir de um esquema TaskCreate.
    """
    # Cria uma instância do modelo Task (ORM) com os dados recebidos
	db_task = models.Task(
		title=task.title,
		description=task.description,
		completed=task.completed,
	)

	# Adiciona a nova tarefa na sessão
	db.add(db_task)
	# Confirma (commit) as alterações no banco
	db.commit()
	# Atualiza o objeto com os dados do banco (id, created_at, etc.)
	db.refresh(db_task)
	return db_task


def update_task(db: Session, db_task: models.Task, updates: schemas.TaskUpdate):
	"""
    Atualiza uma tarefa existente com os dados enviados em TaskUpdate.
    db_task: objeto Task já buscado do banco
    updates: campos que desejamos atualizar
    """
    # Só atualiza os campos que não são None
	if updates.title is not None:
		db_task.title = updates.title
	if updates.description is not None:
		db_task.description = updates.description
	if updates.completed is not None:
		db_task.completed = updates.completed

	# Salva as alterações
	db.commit()
	# Atualiza o objeto com os dados mais recentes do banco
	db.refresh(db_task)
	return db_task


def delete_task(db: Session, db_task: models.Task):
	"""
    Remove uma tarefa do banco de dados.
    """
	db.delete(db_task)
	db.commit()
