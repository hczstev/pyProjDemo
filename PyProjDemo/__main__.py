from PyProjDemo.Foo import foo
from PyProjDemo import __version__

if __name__ == "__main__":
    print("version: ", __version__)
    foo.callBar()
