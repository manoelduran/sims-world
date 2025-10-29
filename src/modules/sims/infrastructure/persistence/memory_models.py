import uuid
from sqlalchemy import (
    Column,
    Text,
    UUID,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from src.core.database import Base


class MemoryModel(Base):
    __tablename__ = "memories"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sim_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), nullable=False)
    description = Column(Text, nullable=False)
    importance_score = Column(Integer, default=5, nullable=False)
    embedding = Column(Vector(768))
    sim = relationship("SimModel", back_populates="memories")
