from app.db.database import (
    SessionLocal
)

from app.core.container import (
    container
)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


def get_chat_service():

    return (
        container.chat_service
    )


def get_rag_service():

    return (
        container.rag_service
    )