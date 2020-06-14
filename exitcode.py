"""
    This script shows how to exit to the shell
    returning a value

    Author: Renato Montenegro Rustici

"""

import sys

try:
    sample_file = open("foo.txt", "r+")
    print(f"File {sample_file} is now open")
    sample_file.close()
    print(f"File {sample_file} is now closed")
    sys.exit(0)

except OSError as systemError:
    print("Error opening file: {0}".format(systemError))
    sys.exit(1)

print("This is unreacheable")
