from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from sqlalchemy.sql import func


from .database import Base


# Modelo ORM que representa a tabela "tasks" no banco de dados
class Task(Base):
	# Nome da tabela no banco
	__tablename__ = "tasks"

	# Colunas de tabelas:
	# id: chave primária, índica para rápida busca
	id = Column(Integer, primary_key=True, index=True)

	# title: título da tarefa, obrigatório (nullable=False, tamanho máximo 100)
	title = Column(String(100), nullable=False)

	# description: descrição opcional (nullable=True)
	description = Column(Text, nullable=True)

	# completed: booleano indicando se a tarefa foi concluída
	# default=False: por padrão, tarefa começa não concluída
	completed = Column(Boolean, nullable=False, default=False)

	# created_at: data/hora de criação da tarefa, preenchida automaticamente
	created_at = Column(DateTime(timezone=True), server_default=func.now())

	# updated_at: data/hora de atualização´, atualizada automaticamente
	updated_at = Column(DateTime(timezone=True), onupdate=func.now())