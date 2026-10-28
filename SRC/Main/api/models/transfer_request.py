from SRC.Main.api.models.base_model import BaseModel
from typing import Annotated
from SRC.Main.api.generators.creation_rule import CreationRule
class TransferRequest(BaseModel):
    fromAccountId: int
    toAccountId: int
    amount: Annotated[int, CreationRule(regex=r"\d+", min_value=1000, max_value=9000)]