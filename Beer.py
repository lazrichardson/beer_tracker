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


def top_score(beer_list, beer_type=None, beer_name=None):
    if beer_type is not None:  # TODO: top beers by type
        print("not implemented")
    if beer_name is not None:  # TODO: search for beers by name
        print("not implemented")
    else:  # TODO: top beers by rating
        top_scoring_beer = beer_list[0]
        for beer in beer_list:
            if beer.rating > top_scoring_beer.rating:
                top_scoring_beer = beer
