#!/usr/bin/env python
"""
This module contains tasks related to arguments & parameters, files in Python.
Please read docstrings and complete the functions.
All functions should returns results of described type.
"""
__author__ = "Pavlo Ivanchyshyn"
__maintainer__ = "Pavlo Ivanchyshyn"
__email__ = "p.ivanchyshyn@gmail.com"
import re
FILENAME = 'awesome_data.info'
lines = [
    "Two assure edward whence the was.",
    "Who worthy yet ten boy denote wonder.",
    "Weeks views her sight old tears sorry.",
    "Additions can suspected its concealed put furnished.",
    "Met the why particular devonshire decisively considered partiality.",
    "Certain it waiting no entered is.",
    "Passed her indeed uneasy shy polite appear denied.",
    "Oh less girl no walk.",
    "At he spot with five of view."
]

USER_INFO = {
    "name": "Pavlo",
    "surname": "Ivanchyshyn",
    "age": 28,
    "city": "Lviv"
}


def find_sum(*args):
    """
    Implement this function!
    This function should sum of numbers for different amount of parameters.

    It should be similar to built-in `sum` function.
    DON'T use `sum` function here.

    Returns:
        int - sum of numbers.

    Examples:
        find_sum(1, 2, 3)  # Returns 6.
        find_sum(1)  # Returns 1.
        find_sum([1, 3])  # Returns 4.
        find_sum(1, 2, 3, 4, 5, 6)  # Returns 21.
        etc.
    """
    # ADD YOUR CODE HERE.
    summary = 0
    for arg in args:
        if isinstance(arg, (list, tuple)):
            for el in arg:
                summary += el
        else:
            summary += arg
    return summary


def write_to_file(filename, data):
    """
    Implement this function!
    This function should write all the lines from `data` into file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    try:
        with open(filename, 'w') as file:
            for element in data:
                file.write(element + '\n')
    except (OSError, IOError):
        print("An Error has occurred!")


def read_file(filename):
    """
    Implement this function!
    This function should read all the lines from the file with `filename`.

    Args:
        filename (str) - name of file for writing.

    Returns:
        list - list of lines from the file.
    """
    # ADD YOUR CODE HERE.

    # my version 1
    # try:
    #     with open(filename, 'r') as file:
    #         text = file.readlines()
    #         return text
    # except (OSError, IOError):
    #     print("An Error has occurred!")

    # my version 2
    try:
        with open(filename, 'r') as file:
            text = file.read()
            text = text.strip().split("\n")
            return text
    except (OSError, IOError):
        print("An Error has occurred!")


# write_to_file(FILENAME, lines)
# read_file(FILENAME)


def append_to_file(filename, data):
    """
    Implement this function!
    This function should append lines from `data` into the file with `filename`.

    Args:
        filename (str) - name of file for writing.
        data (list, tuple) - lines of text which should be added into file.
    """
    # ADD YOUR CODE HERE.
    try:
        with open(filename, 'a') as file:
            for line in data:
                file.write(line + "\n")
    except (OSError, IOError):
        print("An Error has occurred!")


def write_user_info(filename, data):
    """
    Using function `write_to_file` do the following:
    - Create file with a `filename` name.
    - Write user's information from `data` into file with `filename` in the following format:

    Hi there!
    My name is <name> <surname>.
    I am <age> years old.
    I live in <city>.

    Where values in `<>` mean the keys from `data` object.

    Args:
        filename (str) - name of file for writing.
        data (dict) - personal user's information.
    """
    # ADD YOUR CODE HERE.
    try:
        user_info = (
            "Hi there!",
            "My name is {} {}.".format(data['name'], data['surname']),
            "I am {} years old.".format(data['age']),
            "I live in {}.".format(data['city']))
    except KeyError:
        print("An error occurred during reading this file")
    write_to_file(filename, user_info)


# write_user_info(FILENAME, USER_INFO)


def get_user_info(filename):
    """
        Using file created by `write_user_info` create a reader. It should be able to read the following format:

        Hi there!
        My name is <name> <surname>.
        I am <age> years old.
        I live in <city>.

        Where values in `<>` mean the keys from `data` object.

        Args:
            filename (str) - name of file for writing.

        Returns
            dict - personal user's information.

        Example:
            get_user_info(FILENAME)  # Returns {"name": "Pavlo", "surname": "Ivanchyshyn", "age": 28, "city": "Lviv"}
    """
    # My I version
    # data = read_file(filename)
    #
    # def search_value(patterns_start, pattern_end, data):
    #     match = re.search(patterns_start, data)
    #     if match:
    #         pos_start_value = match.end()
    #         match2 = re.search(pattern_end, data)
    #         if match2:
    #             pos_end_value = match2.start()
    #             value = data[pos_start_value:pos_end_value]
    #             return value
    #
    # name = search_value(r"(\s[a-z][a-z]\s)", r"(\s[A-Z]([a-z]+)\.)", data[1])
    # surname = search_value(r"(\s[A-Z]([a-z]+)\s)", r"\.\n", data[1])
    # age = search_value(r"(\s[a-z][a-z]\s)", r" years", data[2])
    # city = search_value(r"(\s[a-z][a-z]\s)", r"\.", data[3])
    # dictionary = {}
    # dictionary['name'] = name
    # dictionary['surname'] = surname
    # dictionary['age'] = age
    # dictionary['city'] = city
    # print(dictionary)
    # return dictionary

    # My II version
    data = read_file(FILENAME)

    for sentence in data:
        sentence = sentence[:-1].strip().split()
        if 'is' in sentence:
            index_el = sentence.index('is')
            name = sentence[index_el + 1]
            surname = sentence[index_el + 2]
        elif 'am' in sentence:
            index_el = sentence.index('am')
            age = sentence[index_el + 1]
        elif 'in' in sentence:
            index_el = sentence.index('in')
            city = sentence[index_el + 1]

    dictionary = {}
    dictionary['name'] = name
    dictionary['surname'] = surname
    dictionary['age'] = age
    dictionary['city'] = city
    return dictionary


# write_user_info(FILENAME, USER_INFO)
# get_user_info(FILENAME)

