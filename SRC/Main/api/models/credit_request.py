from SRC.Main.api.models.base_model import BaseModel
from typing import Annotated
from SRC.Main.api.generators.creation_rule import CreationRule
class CreditRequest(BaseModel):
    accountId: int
    amount: Annotated[int,CreationRule(regex="...", min_value=5000, max_value=15000)]
    termMonths: Annotated[int, CreationRule(regex=r"\d+", min_value=1, max_value=60)]