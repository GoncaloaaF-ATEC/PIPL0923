from fastapi import FastAPI

from modelo import User

app = FastAPI()

usr = User(id=1, user_name="usrTeste", email="mail2@atec.pt")


# TODO: ?

@app.get("/setup")
async def setup():
    # cirar um user
    # garantir que nao ha id duplicados
    usr = User(id=1, user_name="usrTeste", email="mail2@atec.pt")
    return {"msg": "a minha 1a api fastAPI"}


@app.get("/")
async def root():
    return {"msg": "a minha 1a api fastAPI"}


@app.get("/infos")
async def infos():
    return {"msg": "Pagina 2"}


# Criar 3 EP estaticos com msg diferentes


@app.get("/infos/{id}")
async def infos_detatalhe(id: int):
    return {"msg": f"infos do id: {id}"}


@app.get("/users")
async def users(pag: int = 1):
    # TODO: Mostrar todos os alunos
    return {"msg": f"Lista de utilizadores", "pag": f"{pag}"}


@app.get("/users/{id}")
async def users(id: int):
    # TODO:  Mostrar o aluno com o id indicado
    return {f"user_id: {id}": my_user}


@app.get("/users2")
async def users2(pag: int = 1, num: int = 10):
    return {
        "msg": f"Lista de utilizadores",
        "pag": f"{pag}",
        "userPagina": f"{num}",
    }


"""  
@app.post("/addUser", status_code=201) 
async def users(id:int, nome:str, email:str): 
    # código
    global my_user
    my_user = User(id=id, user_name=nome, email=email)
    return {"Adicionado": my_user} 
"""


@app.post("/addUser", status_code=201)
async def users(user: User):
    # TODO:  adicionar alunos a uma lista de alunos
    global my_user
    my_user = user
    return {"Adicionado": my_user}
