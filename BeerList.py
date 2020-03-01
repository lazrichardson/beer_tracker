"""
Luther Richardson
CS521 - February 29th, 2020
Final Project
Command line beer tracker
"""
import csv
import Beer
from operator import attrgetter


class BeerList:
    """
    This class manipulates a list of Beer objects from the Beer class
    It includes file import/export, table presentation, and sort algorithms
    """

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

    def __sort_by_rating(self):
        """
        Sorts all beers in the list by their rating
        :return: beer list sorted by rating
        """
        self.beer_list = sorted(self.beer_list, key=attrgetter('rating'),
                                reverse=True)

    def get_beer_list(self):
        """Getter for the main beer list
        :return: list of beers
        """
        return self.beer_list

    def add_beer(self):
        """
        Adds a beer to the beer list from user input
        :return: N/A
        """
        name = input("Input a beer name: ")

        input_ok = False

        rating = 0
        while input_ok is False:
            rating = input("Input your rating (1 to 5): ")

            try:
                rating = int(rating)
                if rating < 1 or rating > 5:
                    print("Not in the right range. Try again")
                else:
                    input_ok = True

            except ValueError:
                print("That's not an integer. Try again.")

        style = input("Input the beer style: ")
        brewer = input("Input the name of the brewer: ")
        brewer_location = input("Input the location of the brewer: ")

        new_beer = Beer.Beer(name, rating, style, brewer, brewer_location)
        self.beer_list.append(new_beer)

    def import_data(self, file_path):
        """
        Imports a file to the beer list from a path; must have headers:
            name, rating, style, brewer, location
        :param file_path: file path where source file exists
        :return: Appends the file to the beer list
        """
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

    def export_data(self):
        """
        Exports data from the beer list to a csv file named
        'beer_list_export.csv'
        :return: data export csv file in working directory
        """
        if len(self.beer_list) < 1:
            print("No values to export...")
        else:
            filename = 'beer_list_export.csv'
            self.__sort_by_rating()
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
            # close the file
            csv_file.close()

            if len(self.beer_list) > 0:
                print(
                    "Exported {:d} rows to file {}".format(len(self.beer_list),
                                                           filename))
            else:
                print("Exported {:d} row to file {}".format(len(self.beer_list),
                                                            filename))

    def top_beers(self, beer_attribute, style_or_name):
        """
        Finds top 5 beers by rating based on the input attribute
        :param beer_attribute: text of the style name or beer name
        :param style_or_name: determines which logic is applied (style/name)
        :return: table listing top 5 beers
        """
        beer_selection = []

        if style_or_name == "style":  # find beers of that style
            for beer in self.beer_list:  # check if beer is of the right style
                if beer_attribute.upper() == beer.get_beer_name().upper():  # case
                    # insensitive
                    beer_selection.append(beer)
        else:
            for beer in self.beer_list:  # find beers matching the name
                if beer_attribute.upper() in beer.get_beer_name().upper():  # case
                    # insensitive
                    beer_selection.append(beer)
        # if nothing added, show error
        if len(beer_selection) < 1:
            print("No results found....")
        else:
            self.__sort_by_rating()
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
                print("{:20} | {:^7} ".format(beer.get_beer_name()
                                              .strip().title(),
                                              beer.star_rating))

    def top_beers_by_rating(self):
        """
        Prints a table of all beers in the beer list sorted by rating
        :return: table of all beers in list sorted by rating
        """
        # sort the beers
        if len(self.beer_list) < 1:
            print("No beers found :(")
        else:
            self.__sort_by_rating()
            print("Here are all the beers sorted by rating...")

            # print out the table
            print("{:^21}|{:^7}".format("Name", "Rating"))
            print("-" * 30)
            for beer in self.beer_list:
                print("{:20} | {:<7} ".format(beer.get_beer_name().title(),
                                              beer.star_rating))
