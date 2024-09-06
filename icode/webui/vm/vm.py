from collections import namedtuple

from engine.shell import ShellClient, ShellResult
from config import Config


def _get_ssh_cli(c):
    cli = ShellClient(name=c.name, host=c.host, port=c.port,
                      user=c.user, passwd=c.password)
    return cli


local = _get_ssh_cli(Config.local)

