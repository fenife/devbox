import json
import requests
import uuid
import datetime
from requests import Response
from loguru import logger


class HttpResult(object):
    def __init__(self, dt: datetime.datetime, req: dict,
                 resp: Response, exc: Exception) -> None:
        self.dt: datetime.datetime = dt
        self.req: dict = req
        self.resp: Response = resp
        self.exc: Exception = exc
        self.method: str = self.req.get("method", "")
        self.url: str = self.req.get("url", "")

    def json(self):
        r = {"dt": str(self.dt),
             "status": None,
             "data": None,
             "exception": str(self.exc)}
        if self.resp is not None:
            r["status"] = self.resp.status_code
            r["data"] = self.resp.json() if len(self.resp.content) > 0 else None
        
        return json.dumps(r)

    def curl(self):
        return self._get_curl_code_snippet()
    
    def _get_curl_code_snippet(self):
        """
        curl -X POST 'service.local:8000/api/v1/user/signup' \
        --header 'Content-Type: application/json' \
        -d '{
            "name": "user1",
            "password": "xxx"
        }'
        """
        req = self.req
        if not req:
            return "curl: None"
        url = self.url
        params = []
        if req.get('params'):
            for k, v in req['params'].items():
                params.append(f"{k}={v}")
        if params:
            url += ','.join(params)
        s = f"curl -X {self.method} '{self.url}'"
        if req.get('headers'):
            for k, v in req['headers'].items():
                s += f" \\\n--header '{k}: {v}' "
        if req.get('body'):
            s += f" \\\n-d '{json.dumps(req['body'], indent=2)}'"
        return s


class HttpClient(object):
    def __init__(self, host: str, port: int) -> None:
        self._host = host
        self._port = port
        self._server = "http://{h}:{p}".format(h=host, p=port)

    def do(self, method: str, url: str, params: dict = {}, body: dict = {},
           headers: dict = {}) -> HttpResult:
        headers.update({
            "x-request-id": str(uuid.uuid1()),
            "Content-Type": "application/json"
        })
        method = method.upper()
        dt = datetime.datetime.now()
        resp = exc = None
        try:
            kwargs = {"headers": headers}
            if params:
                kwargs["params"] = params
            if body:
                kwargs["body"] = body
            if method == "GET":
                resp = requests.get(url=url, **kwargs)
                # resp = requests.get(url=url, headers=headers, params=params)
            elif method == "POST":
                resp = requests.post(url=url, **kwargs)
                # resp = requests.post(url=url, headers=headers, params=params, json=body)
            elif method == "PUT":
                resp = requests.put(url=url, **kwargs)
                # resp = requests.put(url=url, headers=headers, params=params, json=body)
            elif method == "DELETE":
                resp = requests.delete(url=url, **kwargs)
                # resp = requests.delete(url=url, headers=headers, params=params, json=body)
            else:
                exc = Exception("unknown method: %s" % method)
        except Exception as e:
            exc = e

        req_dict = {"method": method, "url": url, "params": params,
                    "body": body, "headers": headers}
        resp_dict = {"exception": str(exc) if exc else None,
                     "status": None, "data": None, "size": None}
        if resp is not None:
            resp_dict["status"] = resp.status_code
            resp_dict["size"] = len(resp.content)
            resp_dict["data"] = resp.json() if len(resp.content) > 0 else None
        msg = json.dumps(
            {"msg": "do http request", "req": req_dict, "resp": resp_dict})
        logger.info(msg)
        result = HttpResult(dt=dt, req=req_dict, resp=resp, exc=exc)
        return result

    def _get_full_path(self, url):
        if not self._server:
            return url
        return self._server + url

    def get(self, url: str, params: dict = {}):
        url = self._get_full_path(url)
        return self.do("GET", url, params=params)

    def post(self, url: str, body: dict = {}, params: dict = {}):
        url = self._get_full_path(url)
        return self.do("POST", url, body=body, params=params)

    def put(self, url: str, body: dict = {}, params: dict = {}):
        url = self._get_full_path(url)
        return self.do("PUT", url, body=body, params=params)

    def delete(self, url: str, body: dict = {}, params: dict = {}):
        url = self._get_full_path(url)
        return self.do("DELETE", url, body=body, params=params)
