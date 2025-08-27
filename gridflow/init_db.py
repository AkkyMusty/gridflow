from .database import Base, engine
from . import models

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created!")

if __name__ == "__main__":
    init_db()
