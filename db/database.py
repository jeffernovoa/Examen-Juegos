from sqlalchemy import create_engine, Column, Integer, String, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class VectorGuardado(Base):
    __tablename__ = 'vectores'
    id = Column(Integer, primary_key=True)
    juego = Column(String)
    vector = Column(PickleType)

engine = create_engine('sqlite:///vectores.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)