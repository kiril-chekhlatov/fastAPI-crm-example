from api.crud.base import CRUDBase
from models.major import Major
from schemas.major import MajorCreate, MajorUpdate


class CRUDMajor(CRUDBase[Major, MajorCreate, MajorUpdate]):
    pass


major = CRUDMajor(Major)
