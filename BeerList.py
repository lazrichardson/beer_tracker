import csv
import Beer
from operator import attrgetter


class BeerList:
    def __init__(self, beer_list):
        self.beer_list = beer_list

    def import_data(self, file_path):
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            output_data = []
            for row in csv_reader:
                output_data.append(row)
            for row in output_data:
                new_beer = Beer.Beer(row["name"], row["rating"], row["style"],
                                     row["brewer"], row["location"])
                self.beer_list.append(new_beer)

    # TODO: Export my data from the tracker via CSV
    def export_data(self):
        print("Not implemented")

    def top_beers_by_type(self, beer_style):
        beer_selection = []
        for beer in self.beer_list:  # check if beer is of the right style
            if beer_style.upper() == beer.style.upper():  # case insensitive
                beer_selection.append(beer)
        if len(beer_selection) < 1:
            print("No results found....")
        else:  # sort the beers
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
    def top_beers_by_name(self, beer_name):

        beer_selection = []

        for beer in self.beer_list:  # check if beer is of the right style
            if beer_name.upper() in beer.name.upper():  # case insensitive
                beer_selection.append(beer)

        if len(beer_selection) < 1:
            print("No results found....")
        else:  # sort the beers
            beer_selection = sorted(beer_selection, key=attrgetter('rating'),
                                    reverse=True)
            print(
                "Here are the top beers with a name like {}  ...".format(
                    beer_name.title()))

            if len(beer_selection) > 5:  # show only the top 5 beers
                beer_selection = beer_selection[0:5]

            print("{:^21}|{:^7}".format("Name", "Rating"))
            print("-" * 30)
            for beer in beer_selection:
                print("{:20} | {:^7} ".format(
                    beer.name.strip().title(),
                    beer.rating))


# TODO: top beers by rating
def top_beers_by_rating(self, beer_style=None, beer_name=None):
    # sort the beers
    self.beer_list = sorted(self.beer_list, key=attrgetter('rating'),
                            reverse=True)
    print("Here are the top 5 beers...".format(beer_style.title()))

    # print out the table
    print("{:^21}|{:^7}".format("Name", "Rating"))
    print("-" * 30)
    counter = 0
    while counter < 5:
        beer = self.beer_list[counter]
        print("{:20} | {:^7} ".format(beer.name.title(), beer.rating))
