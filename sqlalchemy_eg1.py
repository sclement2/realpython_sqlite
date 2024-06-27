from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
#from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///books.db')
print(engine)

metadata_obj = MetaData()
#Base = declarative_base()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)
#class Author(Base):
#    __tablename__ = 'author'
#    id = Column(Integer, primary_key=True)
#    first_name = Column(String)
#    last_name = Column(String)

#Base.metadata.create_all(engine)