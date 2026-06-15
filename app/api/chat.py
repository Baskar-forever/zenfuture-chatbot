from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.api.dependencies import (
    get_db,
    get_chat_service
)

from app.schemas.chat import (
    ChatRequest,
    ChatResponse
)

from app.schemas.session import (
    SessionResponse
)


router = APIRouter(
    prefix="/api",
    tags=["Chat"]
)


@router.post(
    "/session",
    response_model=SessionResponse
)
def create_session(
    db: Session = Depends(get_db),
    chat_service=Depends(
        get_chat_service
    )
):

    return (
        chat_service.create_session(
            db
        )
    )


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    chat_service=Depends(
        get_chat_service
    )
):

    return (
        chat_service.process_message(
            db=db,
            session_id=
                request.session_id,
            message=
                request.message
        )
    )

