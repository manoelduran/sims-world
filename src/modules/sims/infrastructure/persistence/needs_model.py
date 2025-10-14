from sqlalchemy import (
    Column,
    UUID,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from src.core.database import Base


class SimNeedsModel(Base):
    __tablename__ = "sim_needs"
    sim_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), primary_key=True)
    hunger = Column(Integer, default=100, nullable=False)
    energy = Column(Integer, default=100, nullable=False)
    social = Column(Integer, default=100, nullable=False)
    hygiene = Column(Integer, default=100, nullable=False)
    sim = relationship("SimModel", back_populates="needs")
