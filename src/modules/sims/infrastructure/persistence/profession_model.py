import uuid
from sqlalchemy import Column, String, UUID, Integer
from sqlalchemy.orm import relationship
from src.core.database import Base


class ProfessionModel(Base):
    __tablename__ = "professions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False, unique=True)
    base_salary = Column(Integer, nullable=False)
    education_required = Column(String(50))
    skill_required = Column(String(100), nullable=False)
    sims = relationship("SimModel", back_populates="profession")
