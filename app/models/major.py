from db.base_class import Base
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Major(Base):
    __tablename__ = 'majors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(BigInteger, nullable=False)
    description = Column(String, nullable=False)
    students = relationship("Student")

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
