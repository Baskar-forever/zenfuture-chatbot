from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.sql import func

from app.db.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)

    session_id = Column(
        Integer,
        ForeignKey("chat_sessions.id")
    )

    role = Column(String(20))

    content = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )