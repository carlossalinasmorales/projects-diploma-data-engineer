from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Resumen(Base):
    __tablename__ = "resumen"
    run_id = Column(String, primary_key=True)
    timestamp = Column(String)
    total_ventas = Column(Integer)
    n_transacciones = Column(Integer)
    ticket_promedio = Column(Integer)
    clientes_unicos = Column(Integer)

class TopProducto(Base):
    __tablename__ = "top_productos"
    sku = Column(String, primary_key=True)
    nombre = Column(String)
    total_vendido = Column(Integer)
