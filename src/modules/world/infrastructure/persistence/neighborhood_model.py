import uuid
import enum
from sqlalchemy import (
    Column,
    String,
    UUID,
    ForeignKey,
    Integer,
    Enum as SQLAlchemyEnum,
)
from sqlalchemy.orm import relationship
from src.core.database import Base


# Enum for database storage
class SocialClassDbEnum(enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"


class NeighborhoodModel(Base):
    __tablename__ = "neighborhoods"  # Traduzido de 'bairros'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)

    # New fields for social simulation
    average_social_class = Column(
        SQLAlchemyEnum(SocialClassDbEnum),
        nullable=False,
        default=SocialClassDbEnum.medium,
    )
    average_cost_of_living = Column(Integer, nullable=False, default=1000)

    city_id = Column(UUID(as_uuid=True), ForeignKey("cities.id"), nullable=False)
    city = relationship("CityModel", back_populates="neighborhoods")

    # Relation: One Neighborhood -> Many Houses
    houses = relationship(
        "HouseModel", back_populates="neighborhood", cascade="all, delete-orphan"
    )
