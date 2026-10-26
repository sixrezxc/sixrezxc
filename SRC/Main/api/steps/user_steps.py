from SRC.Main.api.fondation.endpoint import Endpoint
from SRC.Main.api.fondation.requesters.validate_crud_requester import ValidateCrudRequester
from SRC.Main.api.models.create_user_request import CreateUserRequest
from SRC.Main.api.models.deposit_request import DepositRequest
from SRC.Main.api.models.transfer_request import TransferRequest
from SRC.Main.api.models.credit_request import CreditRequest
from SRC.Main.api.models.credit_repay_request import CreditRepayRequest
from SRC.Main.api.specs.request_specs import RequestSpecs
from SRC.Main.api.specs.response_specs import ResponseSpecs
from SRC.Main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username = create_user_request.username, password = create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response
    def deposit(self, deposit_request: DepositRequest, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers (username = create_user_request.username, password = create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok(),
        ).post(deposit_request)
        return response
    def transfer(self,  transfer_request: TransferRequest, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers (username = create_user_request.username, password = create_user_request.password),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.request_ok(),
        ).post(transfer_request)
        return response

    def credit(self, credit_request: CreditRequest, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_ACCOUNT,
            ResponseSpecs.request_created(),
        ).post(credit_request)
        return response
    def credit_repay(self, credit_repay_request: CreditRepayRequest, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REPAY_ACCOUNT,
            ResponseSpecs.request_ok(),
        ).post(credit_repay_request)
        return response

