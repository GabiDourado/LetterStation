#fazer fastAPI como o do sor, mas para tudo, criar, alterar e deletar: usuário

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from database import Base, Session, engine
from auth import Usuario


app = FastAPI()

Base.metadata.create_all(engine)


class UsuarioPayload(BaseModel):
#     nome: str
#     curso: str


@app.get("/usuarios", status_code=status.HTTP_200_OK)
def listar_usuarios():
    db = Session()
    usuarios = db.query(Usuarios).all()
    db.close()

    return usuarios


@app.get("/usuarios/{usuarios_id}", status_code=status.HTTP_200_OK)
# def buscar_usuarios(usuarios_id: int):
#     db = Session()
#     usuarios = db.query(Usuarios).filter(Usuarios.id == usuarios_id).first()
#     db.close()

#     if usuarios is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Usuarios não encontrado"
#         )

#     return usuarios


# @app.post("/usuarios", status_code=status.HTTP_201_CREATED)
# def cadastrar_usuarios(dados: UsuariosPayload):
#     db = Session()

#     usuarios = Usuarios(
#         nome=dados.nome,
#         curso=dados.curso
#     )

#     db.add(usuarios)
#     db.commit()
#     db.refresh(usuarios)
#     db.close()

#     return usuarios


# @app.delete("/usuarios/{usuarios_id}", status_code=status.HTTP_204_NO_CONTENT)
# def excluir_usuario(usarios_id: int):
#     db = Session()
#     usuarios = db.query(Usuarios).filter(Usuarios.id == usuarios_id).first()

#     if aluno is None:
#         db.close()
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Usuario não encontrado"
#         )

#     db.delete(usuario)
#     db.commit()
#     db.close()