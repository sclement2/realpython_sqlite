from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///books.db')
print(engine)

Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

Base.metadata.create_all(engine)