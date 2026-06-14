from app.db.database import engine
from app.db.base import Base

print(Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)

print("Done")