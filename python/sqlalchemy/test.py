from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey

engine = create_engine("sqlite:///./sql_app.db", echo=True)
# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     a=conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
#     )
#     conn.commit()
#     print(a)
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

