import pytest
from sqlalchemy.orm import Session
from SRC.Main.api.db.crud.accout_crud import AccountCrudDb as Account
from SRC.Main.api.classes.api_manager import ApiManager
from SRC.Main.api.models.create_user_request import CreateUserRequest
from SRC.Main.api.models.deposit_request import  DepositRequest


@pytest.mark.api
class TestDeposit:
        def test_deposit(self, api_manager:ApiManager, create_user_request: CreateUserRequest, db_session: Session):
            response = api_manager.user_steps.create_account(create_user_request)

            assert response.balance == 0

            deposit_request = DepositRequest(accountId=response.id, amount=1400.5)
            response = api_manager.user_steps.deposit(deposit_request, create_user_request)

            assert response.balance == 1400.5
            account_from_db = Account.get_account_by_id(db_session, response.id)
            assert account_from_db.id == response.id, 'Аккаун не создан,id аккаунт а нет в БД'
            assert account_from_db.balance is not None, 'Поле баланса для созданного аккаунта отсутствует в БД'

