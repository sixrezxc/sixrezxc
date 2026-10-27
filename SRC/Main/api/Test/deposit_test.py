
import pytest

from SRC.Main.api.classes.api_manager import ApiManager
from SRC.Main.api.models.deposit_request import DepositRequest
from SRC.Main.api.models.create_credit_user_request import CreateUserCreditRequest
from SRC.Main.api.generators.model_generator import RandomModelGenerator


@pytest.mark.api
class TestDeposit:

    def test_deposit(self,api_manager: ApiManager,create_credit_user_request: CreateUserCreditRequest):
        account_response = api_manager.user_steps.create_account(create_credit_user_request)

        assert account_response.balance == 0,"Баланс нового счёта должен быть равен 0"

        deposit_request = RandomModelGenerator.generate(DepositRequest)
        deposit_request.accountId = account_response.id

        deposit_response = api_manager.user_steps.deposit(deposit_request,create_credit_user_request)

        assert deposit_response.balance == deposit_request.amount,"После пополнения баланс должен увеличиться на сумму пополнения"
