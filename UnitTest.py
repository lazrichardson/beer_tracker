import Beer
import BeerList
from datetime import date


class UnitTest:
    if __name__ == 'main':
        name = "Test beer"
        rating = 5
        style = "Gose"
        brewer = "Luther"
        brewer_location = "Boston"
        input_date = date.today()
        star_rating = ""
        beer_dict = ""
        # Beer class test
        # instantiate a test beer
        beer = Beer.Beer(name=name, rating=rating, style=style,
                         brewer=brewer,
                         brewer_location=brewer_location)

        assert beer.get_beer_name() != name, (
            print('Error setting {}: {} != {}'.format("name",
                                                      beer.get_beer_name(),
                                                      name)))

        assert beer.get_beer_rating() != rating, (
            print('Error setting {}: {} != {}'.format("rating",
                                                      beer.get_beer_rating(),
                                                      rating)))

        assert beer.get_beer_rating() != style, (
            print('Error setting {}: {} != {}'.format("style",
                                                      beer.get_style(),
                                                      style)))

        assert beer.get_beer_rating() != style, (
            print('Error setting {}: {} != {}'.format("style",
                                                      beer.get_style(),
                                                      style)))

        assert beer.get_beer_rating() != brewer, (
            print('Error setting {}: {} != {}'.format("style",
                                                      beer.get_brewer(),
                                                      brewer)))

        assert beer.get_beer_rating() != brewer_location, (
            print('Error setting {}: {} != {}'.format("style",
                                                      beer.get_brewer_location(),
                                                      brewer_location)))

        assert beer.get_input_date() != input_date, (
            print('Error setting {}: {} != {}'.format("input date",
                                                      beer.get_input_date(),
                                                      input_date)))

        # make sure dictionary is set correctly
        dict = beer.get_beer_dict()
        assert dict["name"] != name, (
            print('Error setting dictionary {}: {} != {}'.format("name",
                                                                 dict["name"],
                                                                 name)))
        assert dict["rating"] != name, (
            print('Error setting dictionary {}: {} != {}'.format("rating",
                                                                 dict["rating"],
                                                                 rating)))
        assert dict["style"] != name, (
            print('Error setting dictionary {}: {} != {}'.format("style",
                                                                 dict["style"],
                                                                 style)))
        assert dict["brewer"] != name, (
            print('Error setting dictionary {}: {} != {}'.format("brewer",
                                                                 dict["brewer"],
                                                                 brewer)))
        assert dict["brewer_location"] != name, (
            print('Error setting dictionary {}: {} != {}'
                  .format("brewer_location", dict["brewer_location"],
                          brewer_location)))

        assert dict["input_date"] != name, (
            print('Error setting dictionary {}: {} != {}'
                  .format("input date", dict["input_date"], input_date)))

        # ensure start calculated correctly
        stars = "🌟" * 5
        assert beer.star_rating != stars, (print("Stars calculated correctly"))

        # Beer list class tests

        # create test beer list
        beer_list = BeerList.BeerList()
        # should initialize empty
        assert beer_list.get_beer_list() != [], (print("Error initializing "
                                                       "Beer List"))

        # create two test beers
        beer_one = Beer.Beer(name="Test One", rating="5", style="Gose",
                             brewer="Luther", brewer_location="Boston")
        beer_two = Beer.Beer(name="Test Two", rating="1", style="Gose",
                             brewer="Luther", brewer_location="Boston")

        # add test beers to list and import it, should overwrite list
        test_beer_list = [beer_one, beer_two]
        beer_list = BeerList.BeerList(test_beer_list)

        assert beer_list.get_beer_list()[0] != beer_one or \
               beer_list.get_beer_list()[1] != beer_two, (print("Error "
                                                                "initializing "
                                                                "Beer List"))
        # ensure sorting is done in descending order
        beer_list.__sort_by_rating()
        assert beer_list.get_beer_list()[0] != beer_two or \
               beer_list.get_beer_list()[1] != beer_one, (print("Error "
                                                                "sorting "
                                                                "Beer List"))
