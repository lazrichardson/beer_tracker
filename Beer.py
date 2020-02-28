from datetime import date
from operator import attrgetter
import csv


class Beer:  # Requirement: User-defined class.

    def __init__(self, name=None, rating=None, style=None, brewer=None,
                 brewer_location=None):
        self.name = name
        self.rating = rating
        self.style = style
        self.brewer = brewer
        self.brewer_location = brewer_location
        self.input_date = date.today()
        self.star_rating = self.__star_printer()
        self.__beer_dict = ""

    def __repr__(self):  # Requirement: implement repr() method
        return repr(
            str(self.name) + str(self.brewer) + str(self.brewer_location) + str(
                self.rating) + str(self.style) + str(
                self.input_date))

    def __set_beer_dict(self):
        beer_dict = {
            "name": self.name,
            "rating": self.rating,
            "style": self.style,
            "brewer": self.brewer,
            "brewer_location": self.brewer_location,
            "input_date": self.input_date}
        self.__beer_dict = beer_dict

    def __star_printer(self):
        return "🌟" * self.rating

    def get_beer_dict(self):
        self.__set_beer_dict()
        return self.__beer_dict

    def get_beer_name(self):
        return self.name

    def get_beer_rating(self):
        return int(self.rating)
