from sqlalchemy.orm import Session
from SRC.Main.api.db.models.transfer_table import  Transfer

class TransferCrudDb:
    @staticmethod
    def get_transfer_account(db: Session, to_account_id: int) -> Transfer | None:
        return db.query(Transfer).filter_by(to_account_id = to_account_id).first()