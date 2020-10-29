from app.crud.base import CRUDBase
from app.models import User
from app.models.role import Role
from sqlalchemy.orm import Session

from app.models import UserRole, User, Role


# class CrudRole(CRUDBase[Role]):
#     def user_role(self, db: Session):
#         pass
        # print("salam man injam")
        # db.query(Role)\
        #     .join(UserRole, Role.id == UserRole.role_id)\
        #     .join(User, UserRole.user_id == User.id)\
        #     .all()


# role = CrudRole(Role)
