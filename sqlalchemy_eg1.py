from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
from sqlalchemy import insert
from sqlalchemy import select, bindparam

engine = create_engine('sqlite:///books.db')
print(engine)

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)

metadata_obj.create_all(engine)

stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
#print(stmt)

compiled = stmt.compile()
#print(compiled.params)

#with engine.connect() as conn:
#    result = conn.execute(stmt)
#    conn.commit()

#with engine.connect() as conn:
#    result = conn.execute(
#        insert(user_table),
#        [
#            {"name": "sandy", "fullname": "Sandy Cheeks"},
#            {"name": "patrick", "fullname": "Patrick Star"},
#        ],
#    )
#    conn.commit()

scalar_subq = (
    select(user_table.c.id)
    .where(user_table.c.name == bindparam("username"))
    .scalar_subquery()
)

#with engine.connect() as conn:
#    result = conn.execute(
#        insert(address_table).values(user_id=scalar_subq),
#        [
#           {"username": "spongebob", "email_address": "spongebob@sqlalchemy.org"},
#            {"username": "sandy", "email_address": "sandy@sqlalchemy.org"},
#            {"username": "sandy", "email_address": "sandy@squirrelpower.org"},
#        ],
#    )
#    conn.commit()

insert_stmt = insert(address_table).returning(
    address_table.c.id, address_table.c.email_address
)
print(insert_stmt)

stmt = select(user_table).where(user_table.c.name == "spongebob")
print(stmt)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)