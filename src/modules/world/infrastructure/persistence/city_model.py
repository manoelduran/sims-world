import uuid
from sqlalchemy import (
    Column,
    String,
    UUID,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from src.core.database import Base


class CityModel(Base):
    __tablename__ = "cities"  # Traduzido de 'cidades'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)

    world_id = Column(UUID(as_uuid=True), ForeignKey("game_worlds.id"), nullable=False)
    world = relationship("GameWorldModel", back_populates="cities")

    # Relation: One City -> Many Neighborhoods
    neighborhoods = relationship(
        "NeighborhoodModel", back_populates="city", cascade="all, delete-orphan"
    )
