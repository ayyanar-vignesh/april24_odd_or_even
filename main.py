"""
Module for checking whether a number is even or odd.

This module provides functionality to determine if a given integer
is even or odd based on divisibility by 2.
"""


def check_even_odd(number):
    """
    Check if a number is even or odd.

    This function takes an integer and determines whether it is even
    (divisible by 2) or odd (not divisible by 2).

    Args:
        number (int): The number to check.

    Returns:
        str: A string indicating whether the number is "even" or "odd".

    Raises:
        TypeError: If the input is not an integer.

    Example:
        >>> check_even_odd(4)
        'even'
        >>> check_even_odd(7)
        'odd'
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")

    if number % 2 == 0:
        return "even number"
    return "odd number"


def main():
    """
    Main function to get user input and display even/odd result.

    Prompts the user to enter a number and prints whether
    the number is even or odd.
    """
    try:
        user_input = int(input("Enter your number: "))
        result = check_even_odd(user_input)
        print(result)
    except ValueError:
        print("Error: Please enter a valid integer.")
    except TypeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
