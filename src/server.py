import typing as t

from fastapi import Depends, FastAPI

from src.deps.database import get_db
from src.infra.database import DataBase
from src.models.message_saver import MessageSaver
from src.schemas.message import MessageCreate

app = FastAPI()


@app.post("/message")
def save_message(message_create: MessageCreate, db: t.Annotated[DataBase, Depends(get_db)]) -> dict[str, t.Any]:
    """..."""
    saver = MessageSaver(message_create, db)
    saver.save_another_message()
    return {}


@app.get("/health")
def health_check() -> str:
    """..."""
    return "OK"


@app.post("/dialogue_opened")
def dialogue_opened() -> dict[str, t.Any]:
    """..."""
    # TODO: отметить отправленные мной сообщения как прочитанные (sent -> read).
    return {}
