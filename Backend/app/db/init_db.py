from pathlib import Path
from app.db.connections import get_connection 

def init_db() -> None:
    schema = (Path(__file__).parent / "schema.sql").read_text()
    conn = get_connection()
    try:
        conn.executescript(schema)
        conn.commit()
    finally:
        conn.close()