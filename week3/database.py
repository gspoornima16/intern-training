from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base;

# DATABASE URL

DATABASE_URL = "postgresql://postgres:Berlin243@localhost:5432/Student"

# ENGINE

engine = create_engine(DATABASE_URL)



# SESSION

SessionLocal = sessionmaker(
    bind=engine,autoflush=False,
    autocommit=False)


# DECLARATIVE BASE
# class Base(DeclarativeBase):
#     pass
Base = declarative_base()