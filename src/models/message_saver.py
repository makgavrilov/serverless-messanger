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

    def save(self) -> None:
        """..."""
        row_data = {
            "from": self.message.from_,
            "to": self.message.to,
            "text": self.message.text,
            "time_to_send": self.message.time_to_send,
            "time_to_receive": self.message.time_to_receive,
        }
        filename = Path.home() / "db" / "messages" / f"{self.message.from_}.csv"
        file_exists = filename.exists()
        with Path(filename).open(mode="a", newline="", encoding="utf-8") as file:
            fieldnames = ["from", "to", "text", "time", "time_to_send", "time_to_receive"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(row_data)
