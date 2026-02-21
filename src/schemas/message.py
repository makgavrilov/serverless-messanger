import datetime
import typing as t
import uuid

from pydantic import BaseModel, Field

MessageStatus = t.Literal["not_sent", "sending", "received", "sent", "read"]


class MessageCreate(BaseModel):
    """..."""

    from_: str = Field(...,alias="from")
    to: str
    text: str
    time_sent: datetime.datetime
    uuid: uuid.UUID


class Message(MessageCreate):
    """..."""

    time_receive: datetime.datetime = Field(default_factory=datetime.datetime.now)
    status: MessageStatus
