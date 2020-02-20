# TODO: at least 1 private and 2 public self attributes
# TODO: at least 1 private and 1 public method that take arguments, return values and are used by your program

from datetime import date


class Beer:  # Requirement: User-defined class.

    def __init__(self):
        self.name = input("Input a beer name: ")
        self.rating = input("Input your rating: ")
        self.style = input("Input the beer style: ")
        self.brewer = input("Input the name of the brewer: ")
        self.brewer_location = input("Input the location of the brewer: ")
        self.input_date = date.today()

    def __repr__(self):  # Requirement: implement repr() method
        return repr(self.name + self.brewer + self.brewer_location + self.rating + self.style + str(self.input_date))


# TODO: Input data via CSV
def import_data(file_path):
    print("Not implemented")


# TODO: Export my data from the tracker via CSV
def export_data():
    print("Not implemented")


def top_beers(beer_list, beer_style=None, beer_name=None):
    if beer_style is not None:  # TODO: top beers by type
        beer_selection = []
        for beer in beer_list:
            if beer_style == beer.style:  # check if beer is of the right type
                beer_selection.append(beer)
        top_beer_list = sorted(beer_selection, key=lambda score: beer.rating)
        return top_beer_list

    elif beer_name is not None:  # TODO: search for beers by name
        beer_selection = []
        for beer in beer_list:
            if beer_name in beer.name:  # check if beer is of the right type
                beer_selection.append(beer)
        top_beer_list = sorted(beer_selection, key=lambda score: beer.rating)
        return top_beer_list

    else:  # TODO: top beers by rating
        top_beer_list = sorted(beer_list, key=lambda score: beer.rating)
        return top_beer_list
