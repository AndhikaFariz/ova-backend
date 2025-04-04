from sqlalchemy.sql import func
from app.database.connection import Base
from sqlalchemy import create_engine, Column, Integer, String, JSON, ForeignKey, DateTime, Text

class UserPreferenceModel(Base):
    __tablename__ = "user_preference"

    user_preference_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("USER.user_id"), nullable=False)
    preferences = Column(JSON, nullable=False)
    last_updated = Column(DateTime(timezone=True), server_default=func.timezone('Asia/Jakarta', func.now()),
                          nullable=False)
    persona = Column(JSON)
    pekerjaan = Column(String)
    usia = Column(Integer)
    marital_status = Column(String)
    penghasilan_perbulan = Column(Integer)