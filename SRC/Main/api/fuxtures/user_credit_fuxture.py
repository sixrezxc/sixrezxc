import pytest
from SRC.Main.api.models.create_credit_user_request import CreateUserCreditRequest
from SRC.Main.api.generators.model_generator import RandomModelGenerator




@pytest.fixture
def create_credit_user_request(api_manager):
    user_request = (RandomModelGenerator.generate(CreateUserCreditRequest))
    api_manager.admin_steps.create_user_request(user_request)
    return user_request