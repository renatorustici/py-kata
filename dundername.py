"""
    This script shows how to call a python script both as an import
    as well as from the shell by checking the variable __name__

    When importing in the REPL, it's possible to call the function
    in one of the following:

    1)
        import dundername
        dundername.do_it()

    2)
        from dundername import do_it
        do_it()

    When calling from the shell the script executes automatically.

    Author: Renato Montenegro Rustici
"""

def do_it():
    print("The function was executed.")
    return

def main(): # Keeps things more organized and intuitive
    do_it()

if __name__ == "__main__": # True when executing from the shell
    main()