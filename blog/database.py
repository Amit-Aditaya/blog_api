from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

SQLALCHEMY_DATABASE_URL = "postgresql://blog_postgres_n1h2_user:qKh1SfczclE4tjuvTlPyqybTsZdwqzVO@dpg-cv5vt88gph6c73dio43g-a.singapore-postgres.render.com/blog_postgres_n1h2"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    #connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()