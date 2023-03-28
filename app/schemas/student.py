from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class StudentBase(BaseModel):
    """ Shared properties """
    name: str
    contract_type: int
    name: str
    surname: str
    middle_name: str
    birth_of_date: date
    email: EmailStr
    address: str
    phone: str
    passport_series: str
    passport_number: str
    PIN: str
    region_id: int
    authority: str
    major_id: int
    gender: int

    discount: bool
    percent: Optional[float] = None
    discount_from: Optional[date] = None
    discount_to: Optional[date] = None

    super_contract: bool
    super_contract_sum: Optional[int] = None

    passport_document: Optional[str] = None
    IELTS_document: Optional[str] = None

    contract_document: Optional[str] = None
    status: Optional[int] = None
    comment_id: Optional[int] = None


class StudentCreate(StudentBase):
    """ Properties to receive on student creation """
    pass


class StudentUpdate(StudentBase):
    """ Properties to receive on student update """
    pass


class StudentInDBBase(StudentBase):
    """ Properties shared by models stored in DB """
    id: int
    contract_document: Optional[str] = None
    time_created: datetime
    time_updated: Optional[datetime] = None

    class Config:
        orm_mode = True


class Student(StudentInDBBase):
    """ Properties to return to client """
    pass


class StudentInDB(StudentInDBBase):
    """ Properties properties stored in DB """
    pass
