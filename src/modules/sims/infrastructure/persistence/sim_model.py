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
    # 1. World ID: A tabela continua sendo 'game_worlds', então isso não muda
    world_id = Column(UUID(as_uuid=True), ForeignKey("game_worlds.id"), nullable=False)

    # 2. Location: Mudou de 'comodos.id' para 'rooms.id'
    # Renomeamos a coluna para manter o padrão em inglês
    current_location_room_id = Column(
        UUID(as_uuid=True), ForeignKey("rooms.id"), nullable=True
    )

    # 3. Relacionamento: Aponta para 'RoomModel' agora
    # O back_populates deve bater com o que definimos em RoomModel ('sims_present')
    current_location = relationship("RoomModel", back_populates="sims_present")
    parent_a_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), nullable=True)
    parent_b_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), nullable=True)
    age_in_days = Column(Integer, nullable=False, default=20)
    life_stage = Column(String(50), nullable=False, default="adult")
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
    profession_id = Column(
        UUID(as_uuid=True), ForeignKey("professions.id"), nullable=True
    )
    profession = relationship("ProfessionModel", back_populates="sims")
    # current_location = relationship("ComodoModel", back_populates="sims_presentes")
    skills = relationship(
        "SkillModel", back_populates="sim", cascade="all, delete-orphan"
    )
    memories = relationship(
        "MemoryModel", back_populates="sim", cascade="all, delete-orphan"
    )
