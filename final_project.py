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
    user_input = input("Enter a selection..."
                       "\n1 to input a new beer"
                       "\n2 to input data from a file"
                       "\n3 to see top beers by a specific style"
                       "\n4 to search for a beer by name"
                       "\n5 to see the top beers overall"
                       "\nE to exit\n...\n")

    if user_input == '1':
        beer_list.append(Beer.Beer())
        print("New beer added...")
    elif user_input == '2':
        input_data = Beer.import_data('test_data')
        for row in input_data:
            new_beer = Beer.Beer(row["name"], row["rating"], row["style"], row["brewer"], row["location"])
            beer_list.append(new_beer)
            # def __init__(self, name=None, rating=None, style=None, brewer=None, brewer_location=None):
    elif user_input == '3':
        print("Here are the beers by type")
    elif user_input == '4':
        beer_search = input("Search for a beer by name:")
        Beer.top_beers(beer_list, None, beer_search)
    elif user_input == '5':
        print("Here are the top beers overall")
    elif user_input == "E":
        print("Goodbye!...")
        break

print(beer_list)
