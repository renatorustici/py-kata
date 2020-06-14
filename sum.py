"""
    This script sums two numbers, presents a result and tells 
    which one is greater and which one is smaller. 
    It explores simple concepts like variables, loops, 
    flow control, functions, strings and integers

    Author: Renato Montenegro Rustici

"""
def sum(x, y):
    result = x + y
    return result
    
while True:
    x = int(input("Type the first number: "))
    y = int(input("Type the second number: "))

    print(f"The first number is {x}")
    print(f"The second number is {y}")

    total = sum(x, y)

    print(f"The sum is {total}")

    should_continue = str(input("Do you want to continue? (y/n) "))

    if should_continue.lower() == "n":
        break

    




