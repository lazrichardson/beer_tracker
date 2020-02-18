# TODO: Beer must be imported by the program
# TODO: at least 1 private and 2 public self attributes
# TODO: at least 1 private and 1 public method that take arguments, return values and are used by your program

from datetime import date


class Beer:  # Requirement: User-defined class.

    def __init__(self, name, brewer, brewer_location, rating, style):
        self.name = name
        self.brewer = brewer
        self.brewer_location = brewer_location
        self.rating = rating
        self.style = style
        self.input_date = date.today()

    def __repr__(self):  # Requirement: implement repr() method
        return repr(self.name + self.brewer + self.brewer_location + self.rating + self.style + self.input_date)


# TODO: Data import of each beer
def beer_input():
    print("Not implemented")


# TODO: Input data via CSV
def import_data(file_path):
    print("Not implemented")


# TODO: Export my data from the tracker via CSV
def export_data(file_path):
    print("Not implemented")


# TODO: top beers by rating
def top_beers_by_rating():
    print("Not implemented")


# TODO: top beers by type
def top_beers_by_type():
    print("Not implemented")


# TODO: search for beers by name
def find_beer_by_name():
    print("Not implemented")
