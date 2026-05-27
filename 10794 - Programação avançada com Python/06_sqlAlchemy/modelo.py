from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    media = Column(Integer)

    def __repr__(self):
        return f"{self.nome} - {self.email}"
