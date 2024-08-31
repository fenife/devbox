from typing import List, Union
import fabric as fab
from invoke import Result, run
from streamlit import logger

class ShellResult(object):
    def __init__(self, pwd: str, result: Result):
        self._pwd = pwd
        self._result = result

    @property
    def origin(self):
        return self._result

    @property
    def pwd(self):
        return self._pwd

    @property
    def cmd(self):
        return self._result.command

    @property
    def stdout(self):
        return self._result.stdout

    @property
    def output(self):
        # text = "%s # %s\n%s\n" % (self.pwd, self.cmd, self.stdout)
        text = "# %s\n%s\n" % (self.cmd, self.stdout)
        return text

class ShellClient(object):
    CMD_ECHO = "echo"
    CMD_PWD = "pwd"
    CMD_CD = "cd"

    def __init__(self, name=None, host=None, port=None, user=None, passwd=None):
        self.is_local = False
        if not host:
            host = "localhost"
            self.is_local = True
        self.host = host
        self.name = name or host
        self.port = port
        self.user = user
        self.passwd = passwd
        self._conn = None
        self._pwd = ""

    @property
    def conn(self) -> fab.Connection:
        if not self._conn:
            if self.is_local:
                self._conn = fab.Connection(host=self.host)
            else:
                self._conn = fab.Connection(
                    host=self.host, user=self.user,
                    connect_kwargs={"password": self.passwd})
        return self._conn

    def runs(self, cmds: Union[str, List[str]], echo=True):
        if isinstance(cmds, str):
            cmds = [cmds]     # str -> [str]
        for cmd in cmds:
            if cmd == self.CMD_ECHO:
                self.echo()
            else:
                self.run(cmd, echo=echo)

    def _run(self, cmd, echo=True) -> Result:
        try:
            if self.is_local:
                resp = self.conn.local(cmd, echo=echo)
            else:
                resp = self.conn.run(cmd, echo=echo)
        except Exception as e:
            print("aaa", e)
            msg = str(e)
            resp = Result(command=cmd, stdout=msg, stderr=msg, exited=-1)

        return resp

    def _build_result(self, resp: Result) -> ShellResult:
        result = ShellResult(pwd=self.pwd, result=resp)
        return result

    def run(self, cmd, echo=True) -> ShellResult:
        resp = self._run(cmd, echo=echo)
        if self.CMD_CD == cmd:
            self.update_pwd()
        result = self._build_result(resp)
        return result

    def echo(self, echo=False):
        return self.run(self.CMD_ECHO, echo=echo)

    @property
    def pwd(self):
        if not self._pwd:
            self.update_pwd()
        return self._pwd

    def update_pwd(self, echo=False):
        result = self._run(self.CMD_PWD, echo=echo)
        pwd = result.stdout.strip()
        if self._pwd != pwd:
            self._pwd = pwd
