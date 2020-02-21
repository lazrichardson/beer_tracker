# TODO: at least 1 private and 2 public self attributes
# TODO: at least 1 private and 1 public method that take arguments, return values and are used by your program

from datetime import date
from operator import attrgetter
import csv


class Beer:  # Requirement: User-defined class.

    def __init__(self, name=None, rating=None, style=None, brewer=None,
                 brewer_location=None):
        if name is not None or rating is not None or style is not None or \
                brewer is not None or brewer_location is not None:
            self.name = name
            self.rating = rating
            self.style = style
            self.brewer = brewer
            self.brewer_location = brewer_location
            self.input_date = date.today()
        else:
            self.name = input("Input a beer name: ")
            self.rating = input("Input your rating: ")
            self.style = input("Input the beer style: ")
            self.brewer = input("Input the name of the brewer: ")
            self.brewer_location = input("Input the location of the brewer: ")
            self.input_date = date.today()

    def __repr__(self):  # Requirement: implement repr() method
        return repr(
            str(self.name) + str(self.brewer) + str(self.brewer_location) + str(
                self.rating) + str(self.style) + str(
                self.input_date))

    def get_beer_name(self):
        return self.name

    def get_beer_rating(self):
        return int(self.rating)


# TODO: Input data via CSV
def import_data(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        output_data = []
        for row in csv_reader:
            output_data.append(row)
        return output_data


# TODO: Export my data from the tracker via CSV
def export_data():
    print("Not implemented")


def top_beers(beer_list, beer_style=None, beer_name=None):
    if beer_style is not None:  # TODO: top beers by type
        beer_selection = []
        for beer in beer_list:  # check if beer is of the right style
            if beer_style.upper() == beer.style.upper():  # case insensitive
                beer_selection.append(beer)
        if len(beer_selection) < 1:
            print("No results found....")
        else:
            # sort the beers
            beer_selection = sorted(beer_selection, key=attrgetter('rating'),
                                    reverse=True)
            print(
                "Here are the top {} style beers...".format(beer_style.title()))

            if len(beer_selection) > 5:  # show only the top 5 beers
                beer_selection = beer_selection[0:5]
            print("{:^21}|{:^7}".format("Name", "Rating"))
            print("-" * 30)
            for beer in beer_selection:
                print("{:20} | {:^7} ".format(
                    beer.name.strip().title(),
                    beer.rating))
    # TODO: search for beers by name
    # TODO: top beers by rating
