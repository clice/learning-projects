from typing import Optional
from datetime import datetime


from pydantic import BaseModel


# TaskBase define os campos em comum entre criação e leitura de tarefas.
# Esse modelo NÃO é diretamente usado na API, mas serve como base
class TaskBase(BaseModel):
	# title é obrigatório
	title: str
	# description é opcional (pode ser None / não enviada)
	description: Optional[str] = None
	# completed tem valor padrão False
	completed: bool = False


# TaskCreate é o esquema usado quando o cliente cria uma tarefa (POST).
# Ele herda tudo de TaskBase sem adicionar nada, mas separa semanticamente.
class TaskCreate(TaskBase):
	pass


# TaskUpdate é usado quando atualizamos uma tarefa (PUT).
# Aqui todos os campos são opcionais, pois podemos mandar só o que queremos alterar.
class TaskUpdate(BaseModel):
	title: Optional[str] = None
	description: Optional[str] = None
	completed: Optional[bool] = None


# Task é o esquema de saída, que a API devolve nas respostas.
# Ele hersa de TaskBase (title, description, completed) e adiciona campos só do banco.
class Task(TaskBase):
	# id vem do banco
	id: int
	# created_at e updated_at são datas vindas do banco, opcionais porque
	# podem estar vazias em alguns momentos. 
	created_at: Optional[datetime] = None
	updated_at: Optional[datetime] = None

	class Config:
		# orm_mode=True permite que o Pydantic converta automaticamente
		# objetos ORM (SQLAlchemy) para esse esquema.
		orm_mode = True