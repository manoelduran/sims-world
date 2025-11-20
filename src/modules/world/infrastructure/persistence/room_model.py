import uuid
from sqlalchemy import (
    Column,
    String,
    UUID,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from src.core.database import Base


class RoomModel(Base):
    __tablename__ = "rooms"  # Traduzido de 'comodos'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255))
    room_type = Column(String(50), nullable=False)  # ex: 'kitchen', 'bedroom'

    house_id = Column(UUID(as_uuid=True), ForeignKey("houses.id"), nullable=False)
    house = relationship("HouseModel", back_populates="rooms")

    # Relation: One Room -> Many Objects
    objects = relationship(
        "ObjectModel", back_populates="room", cascade="all, delete-orphan"
    )

    # Relation: Sims currently inside this room (Cross-module relation)
    # Note: We use string "SimModel" to avoid circular imports if possible,
    # but verify if SimModel has 'current_location' pointing here.
    sims_present = relationship("SimModel", back_populates="current_location")
