import pytest

from SRC.Main.api.classes.api_manager import ApiManager
from SRC.Main.api.models.credit_request import CreditRequest
from SRC.Main.api.models.credit_repay_request import CreditRepayRequest
from SRC.Main.api.models.create_credit_user_request import CreateUserCreditRequest
from SRC.Main.api.generators.model_generator import RandomModelGenerator


@pytest.mark.api
class TestCreditRepay:

    def test_credit_repay(self,api_manager: ApiManager,create_credit_user_request: CreateUserCreditRequest):
        account_response = api_manager.user_steps.create_account(create_credit_user_request)
        assert account_response.balance == 0,"Баланс нового счёта должен быть равен 0"
        credit_request = RandomModelGenerator.generate(CreditRequest)
        credit_request.accountId = account_response.id

        credit_response = api_manager.user_steps.credit(credit_request,create_credit_user_request)

        assert credit_response.balance == credit_request.amount,"После выдачи кредита баланс должен увеличиться на сумму кредита"

        repay_request = RandomModelGenerator.generate(CreditRepayRequest)
        repay_request.creditId = credit_response.creditId
        repay_request.accountId = account_response.id
        repay_request.amount = credit_request.amount

        repay_response = api_manager.user_steps.credit_repay(repay_request,create_credit_user_request)
        assert repay_response.balance == 0