from __future__ import annotations

import typing as t

from src.schemas.message import Message, MessageCreate, MessageStatus

if t.TYPE_CHECKING:
    from src.infra.database import DataBase


class MessageSaver:
    """..."""

    def __init__(self, message_create: MessageCreate, db: DataBase) -> None:
        """..."""
        self.message_create = message_create
        self.db = db

    def save_my_message(self) -> None:
        """..."""
        username = self.message_create.to
        self._save_message(username, "sending")

    def save_another_message(self) -> None:
        """..."""
        username = self.message_create.from_
        self._save_message(username, "received")

    def _save_message(self, username: str, status: MessageStatus) -> None:
        """Сохранение сообщения.

        not_sent - response.status_code != 200 or timeout для POST /message
        sending - когда сообщение было отправлено, но сервер ещё не ответил
        received - любое сообщение, полученое с помощью метода POST /message
        sent - response.status_code == 200 для POST /message
        read - когда собеседник открыл чат и сообщил об этом.
        """
        message = Message(**self.message_create.model_dump(by_alias=True), status=status)
        message_dump = message.model_dump(mode="json")
        self.db.create_table_for_user(username)
        self.db.save_message(username, message_dump)
