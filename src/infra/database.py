from __future__ import annotations

import typing as t

if t.TYPE_CHECKING:
    import sqlite3


class DataBase:
    """..."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        """..."""
        self.connection = connection

    def create_table_for_user(self, username: str) -> None:
        """..."""
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {username} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                "from" TEXT NOT NULL,
                "to" TEXT NOT NULL,
                text TEXT NOT NULL,
                time_sent TEXT NOT NULL,
                time_received TEXT NOT NULL,
                status TEXT NOT NULL,
                uuid TEXT NOT NULL
            )
        """,
        )
        self.connection.commit()

    def save_message(self, username: str, message: dict[str, t.Any]) -> None:
        """..."""
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            INSERT INTO "{username}" ("from", "to", text, time_sent, time_received, status, uuid)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            (
                message["from_"],
                message["to"],
                message["text"],
                message["time_sent"],
                message["time_receive"],
                message["status"],
                message["uuid"],
            ),
        )
        # TODO: использовать именованные параметры
        self.connection.commit()
