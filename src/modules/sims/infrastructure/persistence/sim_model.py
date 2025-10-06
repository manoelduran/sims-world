import uuid
from sqlalchemy import Column, String, Text, UUID, Integer, Boolean, TIMESTAMP, ForeignKey
from src.core.database import Base

class SimModel(Base):
    __tablename__ = "sims"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    world_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String(255), nullable=False)
    personality_summary = Column(Text, nullable=True)
    parent_a_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), nullable=True)
    parent_b_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), nullable=True)
    age_in_days = Column(Integer, nullable=False, default=20)
    life_stage = Column(String(50), nullable=False, default='jovem_adulto')
    is_alive = Column(Boolean, nullable=False, default=True)
    death_date = Column(TIMESTAMP(timezone=True), nullable=True)