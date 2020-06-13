"""
    This script shows how to exit to the shell
    returning a value

    Author: Renato Montenegro Rustici

"""

import sys

try:
    fSample = open("foo.txt", "r+")
    print(f"File {fSample.name} is now open")
    fSample.close()
    sys.exit(0)
except OSError as systemError:
    print("Error opening file: {0}".format(systemError))
    sys.exit(1)

print("This is unreacheable")
