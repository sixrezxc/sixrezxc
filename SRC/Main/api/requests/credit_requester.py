
from SRC.Main.api.models.credit_request import CreditRequest
from SRC.Main.api.models.credit_response import CreditResponse
from SRC.Main.api.requests.requester import Requester
import requests

class CreditRequester(Requester):
    def post(self, credit_request: CreditRequest) -> CreditResponse:
        url = f'{self.base_url}/credit/request'
        response = requests.post(
            url=url,
            json=credit_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return CreditResponse(**response.json())
