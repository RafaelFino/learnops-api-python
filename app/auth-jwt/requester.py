import requests
from logger import Logger
from http import HTTPStatus
import json

class Requester:
    def Execute(method, url, headers={}):
        Logger.Info(f">>> [{method}] {url} -> Headers: {headers}")

        response = requests.request(method=method, url=url, headers=headers)

        ret = response.json()
        ret['status_code'] = response.status_code
        msg = f"<<< [{method}] Respose: {HTTPStatus(response.status_code).name}:{response.status_code}\n Headers:\n\t{response.headers}\n Body:\n\t{json.dumps(ret)}"

        if response.status_code == HTTPStatus.OK:
            Logger.Success(msg)
        else:
            Logger.Error(msg)

        return ret