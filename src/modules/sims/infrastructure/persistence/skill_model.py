from sqlalchemy import (
    Column,
    String,
    UUID,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from src.core.database import Base


class SkillModel(Base):
    __tablename__ = "skills"
    sim_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), primary_key=True)
    skill_name = Column(String(50), primary_key=True)
    level = Column(Integer, default=0, nullable=False)
    sim = relationship("SimModel", back_populates="skills")
