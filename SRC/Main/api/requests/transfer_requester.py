from requests import Response
from SRC.Main.api.models.transfer_request import TransferRequest
from SRC.Main.api.models.transfer_response import  TransferResponse
from SRC.Main.api.requests.requester import Requester
import requests

class TransferRequester(Requester):
    def post(self, transfer_request: TransferRequest) -> TransferResponse:
        url = f'{self.base_url}/account/transfer'
        response = requests.post(
            url=url,
            json=transfer_request.model_dump(),
            headers=self.headers
        )
        self.response_spec(response)
        return TransferResponse(**response.json())