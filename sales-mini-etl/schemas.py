from datetime import datetime
from pydantic import BaseModel

class ResumenSchema(BaseModel):
    run_id: str
    timestamp: datetime
    total_ventas: int
    n_transacciones: int
    ticket_promedio: int
    clientes_unicos: int


class TopProductoSchema(BaseModel):
    sku: str
    nombre: str
    total_vendido: int


class TopProductosResponseSchema(BaseModel):
    top_productos: list[TopProductoSchema]
