"""
LAB 1 Code - Printing an animal with a message
"""


def print_cat(name: str):
    """
    Print a cat ASCII art with a personalized greeting.

    Parameters
    ----------
    name : str
        The name to be included in the greeting.

    Returns
    -------
    None

    Examples
    --------
    >>> print_cat('Alice')
                            /)
                  /\\___/\\ ((  __ Hello, Alice!
                  \\`@_@'/  ))
                  {_:.Y:.}_//
    --------------{{_}}^-'{{_}}----------
    """
    print(f"""                       /)
              /\\___/\\ ((  __ Hello, {name}!
              \\`@_@'/  ))
              {{_:Y:.}}_//
--------------{{_}}^-'{{_}}----------""")


def print_dog(name: str):
    """
    Print a dog ASCII art with a personalized greeting.

    Parameters
    ----------
    name : str
        The name to be included in the greeting.

    Returns
    -------
    None

    Examples
    --------
    >>> print_dog('Bob')
                       __
                  (___()'`;  __ Hello, Bob!
                  /,    /`
                  \\\\"--\\\\""
    """
    print(f"""                   __
              (___()'`;  __ Hello, {name}!
              /,    /`
              \\\\"--\\\\""")


if __name__ == "__main__":
    user_name = input("Please enter your name: ")
    user_animal = input("Would you like a dog or a cat? ")
    if user_animal.lower() == "dog":
        print_dog(user_name)
    elif user_animal.lower() == "cat":
        print_cat(user_name)
    else:
        print("You have entered an incorrect animal!")
