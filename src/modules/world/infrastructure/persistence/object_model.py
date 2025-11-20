import uuid
from sqlalchemy import (
    Column,
    String,
    UUID,
    ForeignKey,
    JSON,
)
from sqlalchemy.orm import relationship
from src.core.database import Base


class ObjectModel(Base):
    __tablename__ = "world_objects"  # Traduzido de 'objetos'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    object_type = Column(String(50), nullable=False)

    room_id = Column(UUID(as_uuid=True), ForeignKey("rooms.id"), nullable=False)
    room = relationship("RoomModel", back_populates="objects")

    state = Column(JSON, nullable=True)
