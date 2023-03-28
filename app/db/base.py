# Import all the models, so that Base has them before being
# imported by Alembic
from db.base_class import Base
from models.comment import Comment
from models.major import Major
from models.region import Region
from models.student import Student
from models.user import User
