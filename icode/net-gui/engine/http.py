import json
import requests
from requests import Response
from loguru import logger


class HttpClient(object):
    def __init__(self, host: str, port: int) -> None:
        self._host = host
        self._port = port
        self._addr = "http://{h}:{p}".format(h=host, p=port)

    def do(self, method: str, url: str, body: dict = {}, params: dict = {},
           headers: dict = {}):
        headers = {
            "Content-Type": "application/json"
        }
        method = method.upper()
        resp = exc = None
        try:
            data = json.dumps(body)
            if method == "GET":
                resp = requests.get(url=url, headers=headers, params=params)
            elif method == "POST":
                resp = requests.post(url=url, headers=headers, data=data, params=params)
            elif method == "PUT":
                resp = requests.put(url=url, headers=headers, data=data, params=params)
            elif method == "DELETE":
                resp = requests.delete(url=url, headers=headers, data=data, params=params)
            else:
                raise Exception("unknown method: %s" % method)
        except Exception as e:
            exc = e

        status_code = content = None
        if resp:
            status_code = resp.status_code
            content = resp.json()
        print(method, url, "body:", body, params, status_code, content, exc)
        return resp

    def get(self, url: str, params: dict = {}):
        url = self._addr + url
        return self.do("GET", url, params=params)

    def post(self, url: str, body: dict = {}, params: dict = {}):
        url = self._addr + url
        return self.do("POST", url, body=body, params=params)

    def put(self, url: str, body: dict = {}, params: dict = {}):
        url = self._addr + url
        return self.do("PUT", url, body=body, params=params)

    def delete(self, url: str, body: dict = {}, params: dict = {}):
        url = self._addr + url
        return self.do("DELETE", url, body=body, params=params)
