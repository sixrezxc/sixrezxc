import pytest

from SRC.Main.api.classes.api_manager import ApiManager
from sqlalchemy.orm import Session
from SRC.Main.api.db.crud.transfer_crud import  TransferCrudDb
from SRC.Main.api.models.create_user_request import CreateUserRequest
from SRC.Main.api.models.deposit_request import  DepositRequest
from SRC.Main.api.models.transfer_request import  TransferRequest

@pytest.mark.api
class TestTransfer:
        def test_transfer(self, api_manager: ApiManager, create_user_request: CreateUserRequest, db_session: Session ):
            one_response = api_manager.user_steps.create_account(create_user_request)

            assert one_response.balance == 0
            deposit_request = DepositRequest(accountId=one_response.id, amount=1000)
            one_response = api_manager.user_steps.deposit(deposit_request, create_user_request)

            assert one_response.balance == 1000

            two_response = api_manager.user_steps.create_account(create_user_request)

            assert two_response.balance == 0

            transfer_request = TransferRequest(fromAccountId=one_response.id, toAccountId=two_response.id, amount=510)
            two_response = api_manager.user_steps.transfer(transfer_request, create_user_request)
            assert two_response.fromAccountIdBalance == 490
            transfer_from_db = TransferCrudDb.get_transfer_account(db_session, two_response.toAccountId)
            assert transfer_from_db is not None
            assert transfer_from_db.amount == transfer_request.amount, 'Сумма не найдена в базе данных'

