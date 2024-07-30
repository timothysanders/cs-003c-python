# CS-003 - LAB 10 - Chapter 9
# 7/29/2024
# Zoraida Rodriguez
# Timothy Sanders
#
# Problem Statement
# Create a class Country that stores the name of the country, its capital,
# its currency, its rate to the dollar, its population, and its area.
# Each instance variable should have an accessor and mutator, along with
# overloaded plus, greater than, equal, int, and str methods
import pytest


class Country:
    ## Initializes the country class and configures the instance variables
    def __init__(
            self,
            name: str = None,
            capital: str = None,
            currency: str = None,
            conversion_rate: float = None,
            population: int = None,
            area_in_square_miles: float = None
    ):
        self._name = name
        self._capital = capital
        self._currency = currency
        self._currency_conversion_rate = conversion_rate
        self._population = population
        self._area_in_square_miles = area_in_square_miles

    ## Retrieves the country name that has been set for the class
    def get_country_name(self) -> str:
        return self._name

    ## Modifies the country name for the class
    #  @param name: str
    #      - The name to set for the country
    def set_country_name(self, name: str) -> None:
        self._name = name

    ## Retrieves the capital name for the class
    def get_country_capital(self) -> str:
        return self._capital

    ## Modifies the capital name for the class
    #  @param name: str
    #      - The name to set for the capital
    def set_country_capital(self, name: str) -> None:
        self._capital = name

    ## Retrieves the currency that has been specified for the class
    def get_currency(self) -> str:
        return self._currency

    ## Sets the currency for the class instance
    #  @param currency: str
    #      - The specified current of the country
    def set_currency(self, currency: str) -> None:
        self._currency = currency

    ## Retrieves the previously specified currency conversion rate
    #  @return None
    def get_currency_conversion_rate(self) -> float:
        return self._currency_conversion_rate

    ## Sets the currency conversion rate for the class instance
    #  @param conversion_rate: float
    #      - The amount of the country’s currency that is converted into $1
    def set_currency_conversion_rate(self, conversion_rate: float) -> None:
        self._currency_conversion_rate = conversion_rate

    ## Retrieves the population of the country class
    def get_population(self) -> int:
        return self._population

    ## Sets the population of the Country class to the given number
    #  @param population: int
    #      - The number to set the population to
    def set_population(self, population: int) -> None:
        self._population = population

    ## Retrieves the area in square miles of the country instance
    def get_area_in_square_miles(self) -> float:
        return self._area_in_square_miles

    ## Sets the area in square miles of the country instance
    #  @param area_in_square_miles: float
    #      - The number to set the area in square miles to
    def set_area_in_square_miles(self, area_in_square_miles: float) -> None:
        self._area_in_square_miles = area_in_square_miles

    ## Overloaded __add__ method to allow us to add populations of countries together
    #  @param other_country: Country
    def __add__(self, other: 'Country') -> 'Country':
        if isinstance(other, Country):
            return Country(population=self._population + other._population)
        else:
            raise NotImplementedError

    ## Overloaded __gt__ method to allow us to compare the areas of two countries
    #  @param other: Country
    def __gt__(self, other: 'Country') -> bool:
        country_greater_than = False
        if self._area_in_square_miles > other._area_in_square_miles:
            country_greater_than = True
        return country_greater_than

    ## Overloaded __eq__ method to compare the currency names and their rates
    #  @param other: Country
    #      - The country to compare currency equality with
    def __eq__(self, other: 'Country') -> bool:
        countries_equal = False
        if (
                self.get_currency() == other.get_currency() and
                self.get_currency_conversion_rate() == other.get_currency_conversion_rate()
        ):
            countries_equal = True
        return countries_equal

    ## Overloaded __int__ method to convert our country object to an integer
    ## equivalent to its population
    def __int__(self) -> int:
        return int(self.get_population())

    ## Overloaded __str__ method to return a string representation of the Country class
    def __str__(self) -> str:
        string_representation = ""
        for name, value in self.__dict__.items():
            string_representation += f"{name[1:]} : {value}\n"
        return string_representation.strip()

    ## Overloaded __repr__ method to return a string representation of the Country class
    def __repr__(self) -> str:
        return self.get_country_name()


def main():
    # Create a list of 5 country objects.
    timland = Country(
        name="Timland",
        capital="Timbuktu",
        currency="Timbuktu Dollar",
        conversion_rate=1.0,
        population=500000,
        area_in_square_miles=100.0
    )
    zoeland = Country(
        name="Zoeland",
        capital="Bruno",
        currency="Bruno Bucks",
        conversion_rate=1.0,
        population=500000,
        area_in_square_miles=200.0
    )
    milesville = Country(
        name="Milesville",
        capital="Chewy City",
        currency="Treats",
        conversion_rate=2.0,
        population=100,
        area_in_square_miles=1.0
    )
    maetown = Country(
        name="Maetown",
        capital="Kitty City",
        currency="Purrs",
        conversion_rate=4.0,
        population=1,
        area_in_square_miles=10.0
    )
    bruno_federation = Country(
        name="Bruno Federation",
        capital="Squirrel City",
        currency="Bruno Bucks",
        conversion_rate=1.0,
        population=50,
        area_in_square_miles=0.1
    )
    country_list = [timland, zoeland, milesville, maetown, bruno_federation]
    print(f"Unsorted list: {country_list}")
    # Go through the list and use the '+' operator to add all the objects and
    # print the result
    total_population = 0
    for country in country_list:
        total_population += country.get_population()
    print(f"Total Population: {total_population}")
    print("Expected: 1000151")
    # Use the sort method of the list to sort your list.
    # Keep in mind sort will use the "greater than" operator for sorting.
    country_list.sort()
    print(f"Sorted List: {country_list}")
    # Start two loops one from the beginning to end -1, and one from the
    # current to the end of the list. Print all countries equal to each other.
    for i in range(len(country_list) - 1):
        for j in range(i + 1, len(country_list)):
            if country_list[i] == country_list[j]:
                print(country_list[i], country_list[j])
    # Print the country with the largest population density
    # (people per square miles).
    # Use the population and area_in_square_miles instance variables.
    highest_density_country = Country()
    highest_density = 0
    for country in country_list:
        density = country.get_population() / country.get_area_in_square_miles()
        if density > highest_density:
            highest_density = density
            highest_density_country = country
    print(f"Highest density country: {repr(highest_density_country)}")
    # Print int version of your largest population density object
    print(f"Highest density country population: {int(highest_density_country)}")
    # Print the whole object of your largest population density object.
    print(f"Highest density country object: {highest_density_country}")


if __name__ == "__main__":
    main()


# UNIT TESTS
def test_add_overload_type():
    country_one = Country(name="Timland", population=100)
    country_two = Country(name="Zoeland", population=200)
    country_total = country_one + country_two
    assert isinstance(country_total, Country)


def test_add_overload_value():
    country_one = Country(name="Timland", population=100)
    country_two = Country(name="Zoeland", population=200)
    country_total = country_one + country_two
    assert country_total.get_population() == 300


def test_add_overload_notimplemented():
    with pytest.raises(NotImplementedError):
        country_one = Country(name="Timland", population=100)
        country_one + 200


def test_eq_overload():
    country_one = Country(name="Zoeland", currency="Dollar", conversion_rate=1.0)
    country_two = Country(name="Timland", currency="Dollar", conversion_rate=1.0)
    assert country_one == country_two


def test_eq_overload_not_equal_currency():
    country_one = Country(name="Zoeland", currency="Dollar", conversion_rate=1.0)
    country_two = Country(name="Timland", currency="Franc", conversion_rate=1.0)
    assert country_one != country_two


def test_eq_overload_not_equal_rate():
    country_one = Country(name="Zoeland", currency="Dollar", conversion_rate=1.0)
    country_two = Country(name="Timland", currency="Dollar", conversion_rate=2.0)
    assert country_one != country_two


def test_gt_overload():
    country_one = Country(name="Zoeland", area_in_square_miles=5000)
    country_two = Country(name="Timland", area_in_square_miles=1000)
    assert country_one > country_two


def test_gt_overload_not_greater():
    country_one = Country(name="Zoeland", area_in_square_miles=500)
    country_two = Country(name="Timland", area_in_square_miles=1000)
    assert not country_one > country_two


def test_int_overload():
    country_one = Country(name="Zoeland", population=5000)
    assert int(country_one) == 5000


def test_str_overload():
    country_one = Country(
        name="Timland",
        capital="Timbuktu",
        currency="Timbuktu Dollar",
        conversion_rate=1.0,
        population=500000,
        area_in_square_miles=100.0
    )
    assert str(country_one) == """name : Timland
capital : Timbuktu
currency : Timbuktu Dollar
currency_conversion_rate : 1.0
population : 500000
area_in_square_miles : 100.0"""


def test_repr_overload():
    country_one = Country(
        name="Timland",
        capital="Timbuktu",
        currency="Timbuktu Dollar",
        conversion_rate=1.0,
        population=500000,
        area_in_square_miles=100.0
    )
    assert repr(country_one) == "Timland"
