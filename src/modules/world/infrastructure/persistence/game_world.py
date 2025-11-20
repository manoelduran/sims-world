import uuid
from sqlalchemy import (
    Column,
    String,
    UUID,
)
from sqlalchemy.orm import relationship
from src.core.database import Base


class GameWorldModel(Base):
    __tablename__ = "game_worlds"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)

    # Relation: One World -> Many Cities
    cities = relationship(
        "CityModel", back_populates="world", cascade="all, delete-orphan"
    )
