"""
Command line beer tracker

## Key Project requirements
- Container type (list, tuple, set, or dictionary)
- Iteration type (for, while)
- Conditional (if)
- Try blocks
TODO: Provide unit tests that prove that your class methods work; should evaluate results using assert statements.
"""
import Beer

beer_list = []
escape = "E"
user_input = ""

while user_input != escape:
    user_input = input("Enter a selection...\n1 to input a new beer\n2 to input data from a file\nE to exit\n...\n")

    if user_input == '1':
        beer_list.append(Beer.Beer())
        print("New beer added...")
    elif user_input == '2':
        Beer.import_data('test_data.csv')
    elif user_input == "E":
        print("Goodbye!...")
        break

print(beer_list)
