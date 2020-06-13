"""
    This script shows how to call a python script both as an import
    as well as from the shell by checking the variable __name__

    When importing in the REPL, it's possible to call the function
    in one of the following:

    1)
        import dundername
        dundername.doIt()

    2)
        from dundername import doIt
        doIt()

    When calling from the shell the script executes automatically.

    Author: Renato Montenegro Rustici
"""

def doIt():
    print("The function was executed.")
    return

if __name__ == '__main__': # True when executing from the shell
    doIt()