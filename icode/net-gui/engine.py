from typing import List, Union
import fabric as fab


class ShellClient(object):
    CMD_ECHO = "echo"

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

    def _run(self, cmd, echo=True):
        if self.is_local:
            return self.conn.local(cmd, echo=echo)
        else:
            return self.conn.run(cmd, echo=echo)

    def run(self, cmds: Union[str, List[str]], echo=True):
        if isinstance(cmds, str):
            cmds = [cmds]     # str -> [str]
        for cmd in cmds:
            if cmd == self.CMD_ECHO:
                self.echo()
            else:
                self._run(cmd, echo=echo)

    def echo(self, echo=False):
        self._run(self.CMD_ECHO, echo=echo)
