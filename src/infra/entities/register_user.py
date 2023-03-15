from src.infra.configs.base import Base
from sqlalchemy import Column, String, Integer, Date


class Users(Base):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name_user = Column(String(50), nullable= False)
    birth_date = Column(Date, nullable= False)
    street = Column(String(25), nullable= False)
    profession = Column(String(25), nullable= False)

    def to_dict(self):
        return {
            "id_user": self.id_user,
            "name_user": self.name_user,
            "birth_date": self.birth_date.isoformat(),
            "street": self.street,
            "profession": self.profession
        }

