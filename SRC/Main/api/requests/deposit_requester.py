from requests import Response
from SRC.Main.api.models.deposit_response import DepositResponse
from SRC.Main.api.models.deposit_request import DepositRequest
from SRC.Main.api.requests.requester import Requester
import requests

class DepositRequester(Requester):
    def post(self, deposit_request: DepositRequest) -> DepositResponse:
        url = f'{self.base_url}/account/deposit'
        response = requests.post(
            url=url,
            json=deposit_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return DepositResponse(**response.json())