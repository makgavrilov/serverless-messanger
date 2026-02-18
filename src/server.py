import typing as t
from pathlib import Path

from fastapi import FastAPI

from models.message_saver import MessageSaver
from schemas.message import Message

app = FastAPI()


(Path.home() / "db").mkdir(parents=True, exist_ok=True)
(Path.home() / "db" / "messages").mkdir(parents=True, exist_ok=True)


@app.post("/message")
def give_message(message: Message) -> dict[str, t.Any]:
    """..."""
    saver = MessageSaver(message)
    saver.save()
    return {}
