from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for model
Base = declarative_base()

# Model definition


class MathRequest(Base):
    __tablename__ = "math_requests"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, nullable=False)     # e.g. "pow"
    parameters = Column(String, nullable=False)    # e.g. "{'base': 2, 'exp': 3}"
    result = Column(Float, nullable=False)         # e.g. 8.0
    timestamp = Column(DateTime, default=datetime.now)


# SQLite database file
DATABASE_URL = "sqlite:///math.db"

# Create the SQLAlchemy engine and session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Initialize DB - call this once at app startup


def init_db():
    Base.metadata.create_all(bind=engine)
