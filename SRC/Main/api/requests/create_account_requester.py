import requests

from SRC.Main.api.models.create_account_response import CreateAccountResponse
from SRC.Main.api.models.create_user_request import CreateUserRequest
from SRC.Main.api.requests.requester import Requester

class CreateAccountRequester(Requester):
    def post(self, model=None) -> CreateAccountResponse:
        url=f"{self.base_url}/account/create"
        response = requests.post(
            url=url,
            headers=self.headers,
        )
        self.response_spec(response)
        return CreateAccountResponse(**response.json())