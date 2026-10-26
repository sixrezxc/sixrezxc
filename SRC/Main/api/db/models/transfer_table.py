from sqlalchemy import Column, Integer, Float ,ForeignKey
from SRC.Main.api.db.base import Base

class Transfer(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True, autoincrement=True)
    to_account_id = Column(Integer, ForeignKey('to_account_id'), nullable=False)
    from_account_id = Column(Integer, ForeignKey('from_account_id'), nullable=False)
    credit_id = Column(Integer, nullable=False, unique=True)
    amount = Column(Float, nullable=False)

    def __repr__(self):
        return f'<Transfer(id={self.id}, to_account_id={self.to_account_id}, from_account_id={self.from_account_id},credit_id={self.credit_id}, amount={self.amount})>'