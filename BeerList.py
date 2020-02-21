import csv
import Beer
from operator import attrgetter


class BeerList:
    def __init__(self, beer_list=None):
        if beer_list is None:
            self.beer_list = []
        else:
            self.beer_list = beer_list

    def __repr__(self):  # Requirement: implement repr() method
        output_string = []
        for beer in self.beer_list:
            output_string.append(str(beer.name) + str(beer.brewer) + str(
                beer.brewer_location) + str(beer.rating) + str(beer.style)
                                 + str(beer.input_date))
        return repr(output_string)

    def add_beer(self):
        new_beer = Beer.Beer()
        self.beer_list.append(new_beer)

    def import_data(self, file_path):
        try:
            with open(file_path) as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=',')
                output_data = []
                for row in csv_reader:
                    output_data.append(row)
                for row in output_data:
                    try:
                        int(row["rating"])
                        new_beer = Beer.Beer(row["name"], int(row["rating"]),
                                             row["style"],
                                             row["brewer"], row["location"])
                        self.beer_list.append(new_beer)
                    except ValueError:
                        print("Row {}'s score is invalid".format(row))
        except FileNotFoundError:
            print("File not found...try again!")

    # TODO: Export my data from the tracker via CSV
    def export_data(self):
        filename = 'beer_list_export.csv'
        with open(filename, 'a', newline='') as csv_file:
            fieldnames = [
                "name",
                "rating",
                "style",
                "brewer",
                "brewer_location",
                "input_date"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for beer in self.beer_list:
                writer.writerow(beer.get_beer_dict())
        print("Exported {:d} rows to file {}".format(len(self.beer_list),
                                                     filename))

    def top_beers(self, beer_attribute, style_or_name):
        beer_selection = []

        if style_or_name == "style":  # find beers of that style
            for beer in self.beer_list:  # check if beer is of the right style
                if beer_attribute.upper() == beer.style.upper():  # case
                    # insensitive
                    beer_selection.append(beer)
        else:
            for beer in self.beer_list:  # find beers matching the name
                if beer_attribute.upper() in beer.name.upper():  # case insensitive
                    beer_selection.append(beer)
        # if nothing added, show error
        if len(beer_selection) < 1:
            print("No results found....")
        else:
            beer_selection = sorted(beer_selection, key=attrgetter('rating'),
                                    reverse=True)
            if style_or_name == "style":
                print("Here are the top {} style beers...".format(
                    beer_attribute.title()))
            else:
                print("Here are the top beers with a name like {}  "
                      "...".format(beer_attribute.title()))

            if len(beer_selection) > 5:  # show only the top 5 beers
                beer_selection = beer_selection[0:5]
            # print the output table
            print("{:^21}|{:^7}".format("Name", "Rating"))
            print("-" * 30)
            for beer in beer_selection:
                print("{:20} | {:^7} ".format(beer.name.strip().title(),
                                              beer.rating))

    # TODO: top beers by rating
    def top_beers_by_rating(self):
        # sort the beers
        self.beer_list = sorted(self.beer_list, key=attrgetter('rating'),
                                reverse=True)
        print("Here are all the beers sorted by rating...")

        # print out the table
        print("{:^21}|{:^7}".format("Name", "Rating"))
        print("-" * 30)
        for beer in self.beer_list:
            print("{:20} | {:^7} ".format(beer.name.title(), beer.rating))
