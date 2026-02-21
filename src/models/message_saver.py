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
        self._save_message("sending")

    def save_another_message(self) -> None:
        """..."""
        self._save_message("received")

    def _save_message(self, status: MessageStatus) -> None:
        """Сохранение сообщения.

        not_sent - response.status_code != 200 or timeout для POST /message
        sending - когда сообщение было отправлено, но сервер ещё не ответил
        received - любое сообщение, полученое с помощью метода POST /message
        sent - response.status_code == 200 для POST /message
        read - когда собеседник открыл чат и сообщил об этом.
        """
        message = Message(**self.message_create.model_dump(by_alias=True), status=status)
        message_dump = message.model_dump(mode="json",by_alias=True)
        self.db.create_table_for_user()
        self.db.save_message(message_dump)
