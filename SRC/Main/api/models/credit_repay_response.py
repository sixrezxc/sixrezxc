from SRC.Main.api.models.base_model import BaseModel
class CreditRepayResponse(BaseModel):
    creditId: int
    amountDeposited: float