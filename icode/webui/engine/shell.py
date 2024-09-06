from typing import List, Union
import fabric as fab
from invoke import Result, run
from streamlit import logger

class ShellResult(object):
    def __init__(self, cli: "ShellClient", result: Result):
        self._cli = cli
        self._result = result

    @property
    def origin(self):
        return self._result

    @property
    def pwd(self):
        return self._cli.pwd

    @property
    def cmd(self):
        return self._result.command

    @property
    def stdout(self):
        return self._result.stdout

    @property
    def stderr(self):
        return self._result.stderr

    @property
    def output(self):
        # text = "%s # %s\n%s\n" % (self.pwd, self.cmd, self.stdout)
        text = f"# {self.cmd}\n{self.stdout or self.stderr}"
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
        self._hostname = ""

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

    # def runs(self, cmds: Union[str, List[str]], echo=True):
    #     if isinstance(cmds, str):
    #         cmds = [cmds]     # str -> [str]
    #     for cmd in cmds:
    #         if cmd == self.CMD_ECHO:
    #             self.echo()
    #         else:
    #             self.run(cmd, echo=echo)

    def _run(self, cmd, echo=True) -> Result:
        try:
            if self.is_local:
                resp = self.conn.local(cmd, echo=echo, warn=True)
            else:
                resp = self.conn.run(cmd, echo=echo, warn=True)
        except Exception as e:
            msg = str(e)
            resp = Result(command=cmd, stdout=msg, stderr=msg, exited=-1)

        return resp

    def _build_result(self, resp: Result) -> ShellResult:
        result = ShellResult(cli=self, result=resp)
        return result

    def run(self, cmd, echo=True) -> ShellResult:
        resp = self._run(cmd, echo=echo)
        result = self._build_result(resp)
        return result

    def echo(self, echo=False):
        return self.run(self.CMD_ECHO, echo=echo)

    @property
    def pwd(self):
        if not self._pwd:
            r = self.run("pwd")
            self._pwd = r.stdout.strip()
        return self._pwd

    @property
    def hostname(self):
        if not self.hostname:
            r = self.run("hostname")
            self._hostname = r.stdout.strip()
        return self._hostname
        

