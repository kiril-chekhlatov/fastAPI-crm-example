from db.base_class import Base
from sqlalchemy import (BigInteger, Boolean, Column, Date, DateTime, Float,
                        ForeignKey, Integer, SmallInteger, String)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    contract_type = Column(SmallInteger, nullable=False)
    name = Column(String(30), index=True, nullable=False)
    surname = Column(String(30), index=True, nullable=False)
    middle_name = Column(String(30), index=True, nullable=False)
    birth_of_date = Column(Date, nullable=False)
    email = Column(String, unique=True, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String(17), nullable=False)
    passport_series = Column(String(2), nullable=False)
    passport_number = Column(String(7), nullable=False)
    PIN = Column(String(14), nullable=False)
    region_id = Column(ForeignKey('regions.id'))
    region = relationship("Region")
    authority = Column(String, nullable=False)
    major_id = Column(ForeignKey('majors.id'))
    major = relationship("Major")
    gender = Column(SmallInteger, nullable=False)

    discount = Column(Boolean, nullable=False)
    percent = Column(Float)
    discount_from = Column(Date)
    discount_to = Column(Date)

    super_contract = Column(Boolean, nullable=False)
    super_contract_sum = Column(BigInteger)

    passport_document = Column(String)
    IELTS_document = Column(String)

    contract_document = Column(String)
    status = Column(SmallInteger, nullable=False, default=1)

    comment_id = Column(ForeignKey('comments.id'))
    comment = relationship("Comment")

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
