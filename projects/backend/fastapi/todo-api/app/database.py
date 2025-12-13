from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# URL de conexão com o banco de dados.
# "sqlite:///./todo.db" significa:
#  - sqlite: usamos o banco SQLite
#  - ///./todo.db: arquivo todo.db na pasta atual do projeto
SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"


# Cria o "engine", que é o objeto principal de conexão com o banco.
# O connect_args={"check_same_thread": False} é necessário para o SQLite
# quando usamos o SQLAlchemy com múltiplas threads (como o Uvicorn).
engine = create_engine(
	SQLALCHEMY_DATABASE_URL,
	connect_args={"check_same_thread": False},
)


# sessionmaker cria uma classe de sessão para conversar com o banco.
# autocommit=False → não faz commit automático
# autoflush=False → não envia alterações automaticamente
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base é a classe base que será herdada pelos modelos ORM (tabelas)
Base = declarative_base()


# Dependência que será usada nas rotas para obter a sessão do banco
def get_db():
	"""
    Dependência do FastAPI que fornece uma sessão de banco de dados
    para cada requisição, e garante que ela seja fechada no final.
    """
	db = SessionLocal()

	try:
		yield db
	finally:
		db.close()