"""
    This script shows some examples on how to work with lists.

    Author: Renato Montenegro Rustici
"""

incremental_list = []

while True:
    item = str(input("Enter something to list or press enter to quit: "))

    if(item == ""):
        break
    
    incremental_list.append(item)

print("\nThis script will add the text \"End of the list\" to the end of the list by pointing to it's index.")

list_length = len(incremental_list)
incremental_list.append("")
incremental_list[list_length] = "End of the list"

print("\nHere is the current state of the list: \n")
print(incremental_list)

item = str(input("\nEnter something to remove from the list or press enter to quit: "))

if(item != ""):
    incremental_list.remove(item)

print("\nHere is the final content of the list: \n")

for idx, item in enumerate(incremental_list):
    print(f"Index {idx}: {item}")

print("\nOne last thing. Let's convert the word LIST into a list: \n")
print(list("LIST"))