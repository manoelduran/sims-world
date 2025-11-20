import uuid
from sqlalchemy import (
    Column,
    String,
    UUID,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from src.core.database import Base


class HouseModel(Base):
    __tablename__ = "houses"  # Traduzido de 'casas'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255))
    address = Column(String(255))

    neighborhood_id = Column(
        UUID(as_uuid=True), ForeignKey("neighborhoods.id"), nullable=False
    )
    neighborhood = relationship("NeighborhoodModel", back_populates="houses")

    # Relation: One House -> Many Rooms
    rooms = relationship(
        "RoomModel", back_populates="house", cascade="all, delete-orphan"
    )
