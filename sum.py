"""
    This script sums two numbers, presents a result and tell 
    which one is greater and which one is smaller. 
    It explores simple concepts like variables, loops, 
    flow control, functions, strings and integers

    Author: Renato Montenegro Rustici

"""
def fSum(iX, iY):
    iResult = iX + iY
    return iResult
    
while True:
    iNum1 = int(input("Type the first number: "))
    iNum2 = int(input("Type the second number: "))

    print(f"The first number is {iNum1}")
    print(f"The second number is {iNum2}")

    iSum = fSum(iNum1, iNum2)

    print(f"The sum is {iSum}")

    strContinue = str(input("Do you want to continue? (y/n) "))

    if strContinue.lower() == "n":
        break

    




