import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print("--- [database.py] Módulo sendo importado...")  # DEBUG PRINT 5
load_dotenv()  # Deixe esta chamada aqui também, por segurança

DATABASE_URL = os.getenv("DATABASE_URL")
print(
    f"--- [database.py] Valor de DATABASE_URL antes de create_engine: '{DATABASE_URL}'"
)  # DEBUG PRINT 6

# A linha que provavelmente está falhando:
try:
    engine = create_engine(DATABASE_URL)
    print("--- [database.py] create_engine bem-sucedido.")  # DEBUG PRINT 7
except Exception as e:
    print(f"--- [database.py] ERRO em create_engine: {e}")  # DEBUG PRINT 8
    raise  # Relança a exceção para vermos o traceback completo
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
