
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
            self.__input_date = date.today()
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
