from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, scoped_session


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str] = mapped_column(String(30))

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan", lazy="subquery"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


# back_populates 两个表 都需要声明
# backref 只声明一个就可以

class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str] = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/sqlalchemy", echo=True)
Base.metadata.create_all(engine)

# with Session(engine) as session:
#
#     spongebob = User(
#         name="spongebob",
#         fullname="Spongebob Squarepants",
#         addresses=[Address(email_address="spongebob@sqlalchemy.org")],
#     )
#     sandy = User(
#         name="sandy",
#         fullname="Sandy Cheeks",
#         addresses=[
#             Address(email_address="sandy@sqlalchemy.org"),
#             Address(email_address="sandy@squirrelpower.org"),
#         ],
#     )
#     patrick = User(name="patrick", fullname="Patrick Star")
#
#     session.add_all([spongebob, sandy, patrick])
#
#     session.commit()

session = Session(engine)
# stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))  # ColumnOperators.in_()   SQL IN 运算符
# for user in session.scalars(stmt):
#     print(user.addresses)

# stmt = (
#     select(Address)
#         .join(Address.user)
#         .where(User.name == "sandy")
#         .where(Address.email_address == "sandy@sqlalchemy.org")
# )
# sandy_address = session.scalars(stmt).one()
#
# stmt = select(User).where(User.name == "patrick")
# patrick = session.scalars(stmt).one()
# patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))
#
# sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"
#
# session.commit()

# sandy = session.get(User, 2)  # 主键获取
# sandy_address = sandy.addresses[0]
# sandy.addresses.remove(sandy_address)
# session.flush()

#
# session.delete(patrick)
# session.commit()


