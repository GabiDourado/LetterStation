from sqlalchemy import Column, Integer, String, Text, Date, Timestamp, timestamp, ForeingKey, Numeric, CheckConstraint
from sqlalchemy.orm import Relationship
from database import Base

class jogo (Base):
      __tablename__ = "jogo"

      id_jogo = Column(Integer, primary_key=True, autoincremente = True)
      id_externo = Column(String(100) nullable= Falce)
      nome = Column(String(255) nullable=Falce)
      descricao = Column (Text)
      data_lancamento = Column (Date)
      capa_url = Column (String(500))
      desenvolvedora = Column(String(255))
      data_atualizacao = Column(Timestamp ,nullable = True)

class usuario (Base):
      __tablename__ = "usuario"

      id_usuario = Column(Integer, primary_key=True,autoincremente=True)
      firebase_uid = Column (String(128) nullable = False, unique = True)
      username = Column (String(30) nullable = False, unique = True)
      email = Column (String(128) nullable = False)
      biografica = Column (String(300))
      avatar_url = Column (String(300))
      data_cadastro = Column (timestamp, nullable = False)
      usu_seg_id = Column (Integer, ForeingKey("usuario_seguidores.usu_seg_id"), nullable =True)

class review (Base):
      __tablaname__ = "review"

      id_avaliacao = Column (Integer, primary_key=True, autoincremente=True)
      id_usuario = Column (Integer, ForeingKey("usuario.id_usuario"), nullable = False)
      id_jogo = Column (Integer, ForeingKey("jogo.id_jogo"), nullable = False)
      nota = Column (Numeric(2,1),nullable = False)
      text = Column (Text)
      data_criacao = Column(Timestamp, nullable=False)
      data_atualizacao = Column(Timestamp, nullable=True)

      __table_args__ =(
            CheckConstraint('nota >= 0 and nota <= 5', name = 'check_nota_range'),
      )
class seguidores (Base):
      __tablaname__ = "seguidores"

      id_seguidores = Column (Integer, primary_key=True,autoincrement=True)
      id_usuario = Column (Integer, ForeingKey("usuario.id_usuario"), nullable = False )
      seguidores_count = Column (Integer)
      

