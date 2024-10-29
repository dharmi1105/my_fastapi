from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Mapped

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String, index=True)
    email: Mapped[str] = Column(String, unique=True, index=True)