from sqlalchemy import (
    Column,
    String,
    UUID,
    Integer,
    ForeignKey,
    CheckConstraint,
)
from src.core.database import Base


class RelationshipModel(Base):
    __tablename__ = "relationships"
    sim_a_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), primary_key=True)
    sim_b_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), primary_key=True)
    relationship_score = Column(Integer, default=0, nullable=False)
    romance_score = Column(Integer, default=0, nullable=False)
    commitment_level = Column(String(50))
    __table_args__ = (CheckConstraint("sim_a_id < sim_b_id"),)
