from sqlalchemy import (
    Column,
    String,
    Text,
    UUID,
    TIMESTAMP,
    ForeignKey,
    BIGINT,
)
from src.core.database import Base


class ActionLogModel(Base):
    __tablename__ = "action_log"
    id = Column(BIGINT, primary_key=True)
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    actor_sim_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"), nullable=False)
    action_type = Column(String(50), nullable=False)
    description = Column(Text)
    target_sim_id = Column(UUID(as_uuid=True), ForeignKey("sims.id"))
