import sqlite3
import typing as t
from pathlib import Path

from src.infra.database import DataBase

DB_PATH = Path.home() / "db" / "messages.db"


def get_db() -> t.Generator[DataBase, None, None]:
    """..."""
    connection = sqlite3.connect(DB_PATH)
    db = DataBase(connection)
    try:
        yield db
    finally:
        connection.close()
