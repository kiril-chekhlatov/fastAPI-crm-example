from api.crud.base import CRUDBase
from models.region import Region
from schemas.region import RegionCreate, RegionUpdate


class CRUDRegion(CRUDBase[Region, RegionCreate, RegionUpdate]):
    pass


region = CRUDRegion(Region)
