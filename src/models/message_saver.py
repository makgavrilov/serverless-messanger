from __future__ import annotations

import csv
import typing as t
from pathlib import Path

if t.TYPE_CHECKING:
    from src.schemas.message import Message


class MessageSaver:
    """..."""

    def __init__(self, message: Message) -> None:
        """..."""
        self.message = message
        self.filename = Path.home() / "db" / "messages"

    def save_my_message(self) -> None:
        """..."""
        self.filename = Path.home() / "db" / "messages" / f"{self.message.to}.csv"
        self._save_message()

    def save_another_message(self) -> None:
        """..."""
        self.filename = Path.home() / "db" / "messages" / f"{self.message.from_}.csv"
        self._save_message()

    def _save_message(self) -> None:
        """..."""
        row_data = {
            "from": self.message.from_,
            "to": self.message.to,
            "text": self.message.text,
            "time_to_send": self.message.time_to_send,
            "time_to_receive": self.message.time_to_receive,
            "status": self.message.status,
        }
        file_exists = self.filename.exists()
        with Path(self.filename).open(mode="a", newline="", encoding="utf-8") as file:
            fieldnames = ["from", "to", "text", "time", "time_to_send", "time_to_receive", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(row_data)
