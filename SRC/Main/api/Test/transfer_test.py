
import pytest
from sqlalchemy.orm import Session

from SRC.Main.api.classes.api_manager import ApiManager
from SRC.Main.api.db.crud.transfer_crud import TransferCrudDb
from SRC.Main.api.models.create_credit_user_request import CreateUserCreditRequest
from SRC.Main.api.models.deposit_request import DepositRequest
from SRC.Main.api.models.transfer_request import TransferRequest
from SRC.Main.api.generators.model_generator import RandomModelGenerator


@pytest.mark.api
class TestTransfer:

    def test_transfer(self,api_manager: ApiManager,create_credit_user_request: CreateUserCreditRequest,db_session: Session):
        sender = api_manager.user_steps.create_account(create_credit_user_request)
        assert sender.balance == 0, "Баланс нового счёта должен быть равен 0"

        deposit_request = RandomModelGenerator.generate(DepositRequest)
        deposit_request.accountId = sender.id

        sender = api_manager.user_steps.deposit(deposit_request, create_credit_user_request)
        assert sender.balance == deposit_request.amount, "После пополнения баланс должен увеличиться на сумму пополнения"

        receiver = api_manager.user_steps.create_account(create_credit_user_request)
        assert receiver.balance == 0, "Баланс счёта получателя должен быть равен 0"

        transfer_request = RandomModelGenerator.generate(TransferRequest)
        transfer_request.fromAccountId = sender.id
        transfer_request.toAccountId = receiver.id
        transfer_request.amount = deposit_request.amount

        transfer_response = api_manager.user_steps.transfer(transfer_request, create_credit_user_request)

        assert transfer_response.fromAccountIdBalance == 0,"После перевода всего остатка баланс отправителя должен быть равен 0"

        transfer_from_db = TransferCrudDb.get_transfer_account(db_session, transfer_response.toAccountId)

        assert transfer_from_db is not None, "Перевод не найден в базе данных"
        assert transfer_from_db.amount == transfer_request.amount,"Сумма перевода в базе данных не совпадает с ожидаемой"


