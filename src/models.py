from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from src.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(25), nullable=False, unique=True)
    password = Column(String(25), nullable=False)


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(120), nullable=False)
    email = Column('email', String(100), nullable=False)
    cell_phone = Column('cell_phone', String(100), nullable=False)


class Notice(Base):
    __tablename__ = 'notices'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    tags = Column(String(100), nullable=True)
    person_id = Column(Integer, ForeignKey('persons.id', ondelete="CASCADE"))
    person = relationship(Person)