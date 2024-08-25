from pprint import pprint
from engine import ShellClient, ShellResult

def ls_current():
    local = ShellClient()
    result = local.run("ls -alh")
    return result


def test_local():
    local = ShellClient()
    result = local.run("ls -alh")
    print("\nresult:")
    pprint(result.__dict__)
    pprint(result.output)


def main():
    test_local()

if __name__ == "__main__":
    main()
