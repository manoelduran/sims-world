import uuid
from sqlalchemy import (
    Column,
    String,
    Text,
    UUID,
    Integer,
    TIMESTAMP,
    ForeignKey,
    BIGINT,
)
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import VECTOR
from src.core.database import Base


class MemoryModel(Base):
    __tablename__ = "memories"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sim_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), nullable=False)
    description = Column(Text, nullable=False)
    importance_score = Column(Integer, default=5, nullable=False)
    embedding = Column(VECTOR(768))
    sim = relationship("SimModel", back_populates="memories")


class ActionLogModel(Base):
    __tablename__ = "action_log"
    id = Column(BIGINT, primary_key=True)
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    actor_sim_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), nullable=False)
    action_type = Column(String(50), nullable=False)
    description = Column(Text)
    target_sim_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"))
    target_object_id = Column(UUID(as_uuid=True), ForeignKey("objetos.id"))
