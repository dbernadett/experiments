from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey

engine = create_engine("sqlite:///./sql_test_orm.db", echo=True)

from sqlalchemy.orm import DeclarativeBase


from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Boolean

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class InviteCode(Base):
    __tablename__ = "invite_code"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String)
    user_id = mapped_column(ForeignKey("user_account.id"))
    used: Mapped[Boolean] = mapped_column(Boolean)
    def __repr__(self) -> str:
        return f"InviteCode(id={self.id!r}, used={self.used!r}, code={self.code!r}, user_id={self.user_id!r})"

print("Beginning Session Shit")
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

connection = engine.connect()
transaction = connection.begin()
session = SessionTesting(bind=connection)

with session.begin():
    userz = session.query(User).filter(User.name == 'David').first()
    print(userz)
if not userz:
    with session.begin():
        print("Press enter to continue:", end="")
        line=input()
        u=User(name="David", fullname="David Bernadett")
        session.add(u)
        session.commit()
david = session.query(User).filter(User.name == "David").first()
print(david)



