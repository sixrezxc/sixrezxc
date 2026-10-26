import pytest
from sqlalchemy.orm import Session
from SRC.Main.api.db.crud.credit_crud import CreditCrudDb
from SRC.Main.api.classes.api_manager import ApiManager
from SRC.Main.api.models.credit_request import CreditRequest
from SRC.Main.api.models.create_credit_user_request import CreateUserCreditRequest



@pytest.mark.api
class TestDeposit:
        def test_credit_request(self, api_manager: ApiManager,create_credit_user_request: CreateUserCreditRequest, db_session: Session):
            response = api_manager.user_steps.create_account(create_credit_user_request)

            assert response.balance == 0

            credit_request = CreditRequest(accountId=response.id, amount=14000, termMonths= 12)
            response = api_manager.user_steps.credit(credit_request, create_credit_user_request)

            assert response.balance == 14000

            credit_from_db = CreditCrudDb.get_credit_by_credit_id(db_session, response.creditId)
            assert credit_from_db is not None, 'id кредита не найдено'
            assert credit_from_db.id == response.creditId