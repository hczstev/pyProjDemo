from PyProjDemo.Foo import foo
from PyProjDemo import __version__
import anyLib
import json
import os
import sys

def main():
    print("version: ", __version__)
    print("first argument: ", sys.argv[1])
    anyLib.anyFunc()
    print("Calling getDouble:", foo.getDouble(5))
    
    with open(os.path.join(os.path.dirname(__file__), "config.json"), "r")as f:
        print("config.json:", json.load(f))

if __name__ == "__main__":
    main()
