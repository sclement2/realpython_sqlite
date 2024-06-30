from sqlalchemy import create_engine
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from sqlalchemy import select

engine = create_engine('sqlite:///books_orm.db')
print(engine)

#with engine.connect() as conn:
#    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#    conn.execute(
#        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
#    )
#    conn.commit()

class Base(DeclarativeBase):
    pass

print(Base.metadata)
print(Base.registry)

metadata_obj = MetaData()

class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

Base.metadata.create_all(engine)

#some_table = Table("some_table", metadata_obj, autoload_with=engine)

print(select(User))
with Session(engine) as session:
    row = session.execute(select(User)).first()
    print(row)
    user = session.scalars(select(User)).first()
    print(user)
    email_list = session.execute(
        select(User.name, Address).where(User.id == Address.user_id).order_by(Address.id)
    ).all()
    print(email_list)
