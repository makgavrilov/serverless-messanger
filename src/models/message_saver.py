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
        self._save_message("sending")

    def save_another_message(self) -> None:
        """..."""
        self.filename = Path.home() / "db" / "messages" / f"{self.message.from_}.csv"
        self._save_message("received")

    # NOTE: not_sent - response.status_code != 200 or timeout для POST /message
    #       sending - когда сообщение было отправлено, но сервер ещё не ответил
    #       received - любое сообщение, полученое с помощью метода POST /message
    #       sent - response.status_code == 200 для POST /message
    #       read - когда собеседник открыл чат и сообщил об этом.
    def _save_message(self, status: t.Literal["not_sent", "sending", "received", "sent", "read"]) -> None:
        """..."""
        row_data = {
            "from": self.message.from_,
            "to": self.message.to,
            "text": self.message.text,
            "time_to_send": self.message.time_to_send,
            "time_to_receive": self.message.time_to_receive,
            "status": status,
        }
        file_exists = self.filename.exists()
        with Path(self.filename).open(mode="a", newline="", encoding="utf-8") as file:
            fieldnames = row_data.keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(row_data)
