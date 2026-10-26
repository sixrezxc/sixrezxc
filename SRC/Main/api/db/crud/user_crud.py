from sqlalchemy.orm import Session
from SRC.Main.api.db.models.user_table import User

class UserCrudDb:
    @staticmethod
    def get_user_be_username(db: Session, username: str) -> User | None:
        return db.query(User).filter_by(username = username).first()