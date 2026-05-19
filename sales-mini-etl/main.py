from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import select
from database import get_session
from models import Resumen, TopProducto
from schemas import ResumenSchema, TopProductosResponseSchema


app = FastAPI(title="Sales Mini ETL API")


@app.get("/")
def hello():
    return "Hola!"


# Endpoint para obtener el resumen de ventas más reciente
@app.get("/resumen", response_model=ResumenSchema)
def get_resumen():
    with get_session() as session:
        row = session.execute(
            select(Resumen).order_by(Resumen.timestamp.desc()).limit(1)
        ).scalar_one_or_none()

    if row is None:
        raise HTTPException(status_code=404, detail="No summary rows found")

    return {
        "run_id": row.run_id,
        "timestamp": row.timestamp,
        "total_ventas": row.total_ventas,
        "n_transacciones": row.n_transacciones,
        "ticket_promedio": row.ticket_promedio,
        "clientes_unicos": row.clientes_unicos,
    }

# Endopoint para obtener los productos más vendidos
@app.get("/top-productos", response_model=TopProductosResponseSchema)
def get_top_productos(n: int = Query(10, ge=1, le=50)):
    with get_session() as session:
        rows = session.execute(
            select(TopProducto).order_by(TopProducto.total_vendido.desc()).limit(n)
        ).scalars().all()

    return {
        "top_productos": [
            {
                "sku": row.sku,
                "nombre": row.nombre,
                "total_vendido": row.total_vendido,
            }
            for row in rows
        ]
    }
