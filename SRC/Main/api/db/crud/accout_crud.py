from sqlalchemy.orm import Session
from SRC.Main.api.db.models.accout_tadle import Account

class AccountCrudDb:
    @staticmethod
    def get_account_by_id(db: Session, account_id: int) -> Account:
        return db.query(Account).filter_by(id=account_id).first()