from sqlalchemy import Column, Integer, String
import database


class Users(database.Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    age = Column(Integer)
    fone = Column(Integer, nullable=False)
