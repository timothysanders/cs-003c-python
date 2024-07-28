# CS-003 - Lab 9.33.13
# 7/25/2024
# Zoraida Rodriguez
# Tim Sanders

# pytest can be installed by running `pip install pytest` in the terminal
import pytest


## Class to create a Moth object with a specific position along an X-axis
class Moth:

    ## Initialize the Moth object with a specific position. The default
    ## position of the Moth object will be ‘0.0’.
    #  @param initial_position: float = 0.0
    #        - A position on an X-axis where the Moth is located
    def __init__(self, initial_position: float = 0.0) -> None:
        if not isinstance(initial_position, (float, int)):
            raise TypeError(
                "initial_position must be one of the types float or int."
            )
        if initial_position < 0:
            raise ValueError(
                "initial_position must be a positive number."
            )
        self._position = initial_position

    ## Moves the Moth object closer to a given light position. When the
    ## move_to_light method is called, the Moth’s new position is halfway
    ## between its old position and the position of the light source.
    #  @param lightPosition: float
    #        - This parameter specifies the location of the light source
    def move_to_light(self, light_position: float) -> None:
        if not isinstance(light_position, (float, int)):
            raise TypeError(
                "light_position must be one of the types float or int."
            )
        if light_position < 0:
            raise ValueError("light_position must be a positive number.")
        if light_position == self._position:
            raise ValueError(
                "You cannot place the light source" \
                "in the same position as your moth!"
            )
        # To obtain the new position of our moth, we take the average of the
        # lightPosition and the current position
        self._position = (light_position + self._position) / 2

    ## Returns the current position of the Moth
    #  @return float
    def get_position(self) -> float:
        return self._position


def main():
    # Create a Moth object with a position of 0.0
    marty_moth = Moth(initial_position=0.0)
    # call our move_to_light method with a position of 4.0
    marty_moth.move_to_light(light_position=4.0)
    # get the current position of our Moth object and print it
    current_position = marty_moth.get_position()
    print(f"Marty Moth's current position is {current_position}.")

    # initialize our Moth class with a position of 2.0
    mary_moth = Moth(initial_position=2.0)
    # call our move_to_light method with a position of 8.0
    mary_moth.move_to_light(light_position=8.0)
    # after moving, get the current position of our Moth object
    current_position = mary_moth.get_position()
    print(f"Mary Moth's current position is {current_position}")


if __name__ == "__main__":
    main()


# UNIT TESTS
# Unit tests can be run by executing `pytest main.py` in the
# terminal after the installation above.

# Test that our Moth class initializes with the appropriate default parameter
def test_moth_init_default_param():
    test_moth = Moth()
    assert test_moth.get_position() == 0.0


# Test that our Moth class initializes with the specified parameter
def test_moth_init_with_param():
    test_moth = Moth(initial_position=2.0)
    assert test_moth.get_position() == 2.0


# Test that our Moth class raises a TypeError when the initial_position
# parameter is not a float or int
def test_moth_init_with_type_error():
    with pytest.raises(TypeError):
        Moth(initial_position="a")


# Test that our Moth class raises a ValueError when the initial_position
# parameter is negative
def test_moth_init_with_value_error():
    with pytest.raises(ValueError):
        Moth(initial_position=-1.0)


# Test that our Moth class raises a TypeError when the lightPosition
# parameter is not a float or int
def test_moth_move_to_light_with_type_error():
    with pytest.raises(TypeError):
        test_moth = Moth()
        test_moth.move_to_light(light_position="one")


# Test that our Moth class raises a ValueError when the lightPosition
# parameter is the same as the current position
def test_moth_move_to_light_with_overlapping_value_error():
    with pytest.raises(ValueError):
        test_moth = Moth()
        test_moth.move_to_light(light_position=0.0)


# Test that our Moth class raises a ValueError when the lightPosition
# parameter is negative
def test_moth_move_to_light_with_negative_value_error():
    with pytest.raises(ValueError):
        test_moth = Moth()
        test_moth.move_to_light(light_position=-1.0)


# Test that our move_to_light method moves the Moth the expected distance
# to the light source
def test_moth_move_to_light():
    test_moth = Moth()
    test_moth.move_to_light(light_position=4.0)
    assert test_moth.get_position() == 2.0


def test_moth_move_to_light_twice():
    test_moth = Moth()
    test_moth.move_to_light(light_position=4.0)
    test_moth.move_to_light(light_position=4.0)
    assert test_moth.get_position() == 3.0
