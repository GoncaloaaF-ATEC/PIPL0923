from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from modelo import Base, Aluno

engine = create_engine('sqlite:///alunos.db')

Base.metadata.create_all(engine)

session = Session(engine)
"""
ctx1 = {
    "nome": "Jose",
    "email": "rui@edu.atec.pt",
    "media": 19
}

usr = [Aluno(**ctx1), Aluno(**ctx1)]

session.add_all(usr)  # adiciona uma lista

ctx1 = {
    "nome": "Jose",
    "email": "rui@edu.atec.pt",
    "media": 19
}

usr2 = Aluno(**ctx1)

session.add(usr2)  # adiciona um elem

session.commit()

"""

stmt = select(Aluno).where(Aluno.media < 10)
# print(stmt)
result = session.execute(stmt)
alunos = result.scalars().all()

for aluno in alunos:
    print(aluno.nome, aluno.email, aluno.media)

alunos[0].media = 15

session.commit()

# faz logo a op
# data = session.query(Aluno).all()
# print(data)
