from sqlalchemy import (
    Column,
    String,
    Text,
    UUID,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from src.core.database import Base


class SimStatusModel(Base):
    __tablename__ = "sim_status"
    sim_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), primary_key=True)
    current_feeling = Column(String(50))
    current_action = Column(Text)
    sim = relationship("SimModel", back_populates="status")
