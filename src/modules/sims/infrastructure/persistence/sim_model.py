import uuid
from sqlalchemy import (
    Column,
    String,
    Text,
    UUID,
    Integer,
    Boolean,
    TIMESTAMP,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from src.core.database import Base


class SimModel(Base):
    __tablename__ = "sims"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    personality_summary = Column(Text)
    world_id = Column(UUID(as_uuid=True), ForeignKey("game_worlds.id"), nullable=False)
    current_location_comodo_id = Column(
        UUID(as_uuid=True), ForeignKey("comodos.id"), nullable=True
    )

    parent_a_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), nullable=True)
    parent_b_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), nullable=True)
    age_in_days = Column(Integer, nullable=False, default=20)
    life_stage = Column(String(50), nullable=False, default="jovem_adulto")
    is_alive = Column(Boolean, nullable=False, default=True)
    death_date = Column(TIMESTAMP(timezone=True), nullable=True)

    needs = relationship(
        "SimNeedsModel",
        back_populates="sim",
        uselist=False,
        cascade="all, delete-orphan",
    )
    status = relationship(
        "SimStatusModel",
        back_populates="sim",
        uselist=False,
        cascade="all, delete-orphan",
    )

    current_location = relationship("ComodoModel", back_populates="sims_presentes")
    skills = relationship(
        "SkillModel", back_populates="sim", cascade="all, delete-orphan"
    )
    memories = relationship(
        "MemoryModel", back_populates="sim", cascade="all, delete-orphan"
    )
