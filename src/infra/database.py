from __future__ import annotations

import typing as t

if t.TYPE_CHECKING:
    import sqlite3


class DataBase:
    """..."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        """..."""
        self.connection = connection

    def create_table_for_user(self) -> None:
        """..."""
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
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

    def save_message(self, message: dict[str, t.Any]) -> None:
        """..."""
        cursor = self.connection.cursor()
        cursor.execute(
            """
            INSERT INTO messages ("from", "to", text, time_sent, time_received, status, uuid)
            VALUES (:from, :to, :text, :time_sent, :time_receive, :status, :uuid)
        """,
            message,
        )
        self.connection.commit()
