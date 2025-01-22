import sqlalchemy as db
from cache.persistence.model import Auth_User  # Correct the import path
from sqlalchemy.orm import Session
import os

class AuthUserRepositroy():

    def __init__(self):
        db_path = os.path.join(os.path.dirname(__file__), '../../db/login.sqlite')
        self.engine = db.create_engine(f'sqlite:///{db_path}', echo=False, future=True)

    def getUserByUserName(self, user_name: str):
        user: Auth_User = None
        with Session(self.engine) as session:
            user = session.query(Auth_User).filter_by(
                username=user_name).first()
        return user

    def insertUser(self, user: Auth_User):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()
