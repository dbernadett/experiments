from operator import and_
from sqlalchemy import select, create_engine
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
    invite_code = relationship("InviteCode", back_populates="user")
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class InviteCode(Base):
    __tablename__ = "invite_code"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String)
    user_id = mapped_column(ForeignKey("user_account.id"))
    used: Mapped[Boolean] = mapped_column(Boolean)
    user = relationship("User", back_populates="invite_code")
    def __repr__(self) -> str:
        return f"InviteCode(id={self.id!r}, used={self.used!r}, code={self.code!r}, user_id={self.user_id!r})"

Base.metadata.create_all(engine)

print("Beginning Session Shit")
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# with SessionTesting.begin() as session:
#     session.add(User(name="David", fullname="David Bernadett"))


# connection = engine.connect()
# transaction = connection.begin()
# session = SessionTesting(bind=connection)
# with session.begin():
#     session.add(User(name="David", fullname="David Bernadett"))  
# transaction.commit()


connection = engine.connect()
session = SessionTesting(bind=connection)
with session.begin():
    user = session.query(User).filter(User.name == "David").first()
    print(user)
if not user:
    with session.begin():
        t=InviteCode(code="XYZ", user_id=None, used=False)
        t2=InviteCode(code="YYZ", user_id=None, used=False)
        session.add(t)
        session.add(t2)
        session.commit()
        session.flush()
  
    with session.begin():
        #ic = session.query(InviteCode).filter(InviteCode.code == "XYZ").first()
        #line=input()
        #if not ic.used:
        print("Press enter to continue:", end="")
        line=input()
        if True:
            
            
            u=User(name="David", fullname="David Bernadett")
            session.add(u)
            session.flush()
            #ic.user=u
            line=input()
            updated=session.query(InviteCode).filter(and_(InviteCode.code == "XYZ", InviteCode.used == False)).limit(1).with_for_update().first()
            #updated=session.execute(select(InviteCode).where(and_(InviteCode.code == "XYZ", InviteCode.used == False)).with_for_update()).fetchone()
            print("----====UPDATED====----")
            print(updated)
            if updated:
                print("----====NEW STUFF====----")
                
                updated.used=True
                updated.user_id = u.id
                print(session.new)
                print("----====DIRTY STUFF====----")
                print(session.dirty)
                print("----====ENTER TO COMMIT====----")
                line=input()
            else:
                raise ValueError("Invite code already used")
else:
    print("User already exists")



