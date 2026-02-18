import datetime

from pydantic import BaseModel


class Message(BaseModel):
    """..."""

    from_: str
    to: str
    text: str
    time_to_send: datetime.datetime | None = None
    time_to_receive: datetime.datetime | None = None
