"""
    This script shows how to retrieve arguments passed from the
    the command line

    Author: Renato Montenegro Rustici
"""
import sys

def show_args():
    print(f"Number os arguments passed: {len(sys.argv)-1}")
    counter = 0

    # It's also possible to access the arguments using argv[index]
    # The first argument, index 0, is the script name
      
    for idx, arg in enumerate(sys.argv):
        # Usually you should use only "for arg in sys.argv"
        # Use the format above to retrieve the index of the args passed
        if idx == 0:
            print(f"The index {idx} holds the value \"{arg}\" which is the name of the script")
        else:
            print(f"The index {idx} holds the argument {counter} and the value is \"{arg}\"")

        counter = counter + 1

def main():
    show_args()

if __name__ == "__main__":
    main()