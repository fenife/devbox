from engine import ShellClient

def test_local():
    local = ShellClient(name="local")
    local.run("whoami")
    local.echo()
    local.run("ls -alh")
    local.echo()

    cmds = ["uname -a", "echo",
            "ps -ef | grep main"]
    local.run(cmds)


def main():
    test_local()


if __name__ == "__main__":
    main()
