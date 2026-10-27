from SRC.Main.api.models.base_model import BaseModel
from typing import Annotated
from SRC.Main.api.generators.creation_rule import CreationRule

class DepositRequest(BaseModel):
    accountId: int
    amount: Annotated[int,CreationRule(regex="...", min_value=1000, max_value=10000)]