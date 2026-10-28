
import pytest
from sqlalchemy.orm import Session

from SRC.Main.api.db.crud.credit_crud import CreditCrudDb
from SRC.Main.api.classes.api_manager import ApiManager
from SRC.Main.api.models.credit_request import CreditRequest
from SRC.Main.api.models.create_credit_user_request import CreateUserCreditRequest
from SRC.Main.api.generators.model_generator import RandomModelGenerator


@pytest.mark.api
class TestCreditRequest:

    def test_credit_request(self,api_manager: ApiManager,
        create_credit_user_request: CreateUserCreditRequest,db_session: Session):
        account_response = api_manager.user_steps.create_account(create_credit_user_request)

        assert account_response.balance == 0

        credit_request = RandomModelGenerator.generate(CreditRequest)
        credit_request.accountId = account_response.id

        credit_response = api_manager.user_steps.credit(credit_request,create_credit_user_request)

        assert credit_response.balance == credit_request.amount

        credit_from_db = CreditCrudDb.get_credit_by_credit_id(db_session,credit_response.creditId)

        assert credit_from_db is not None, 'id кредита не найдено'
        assert credit_from_db.id == credit_response.creditId
