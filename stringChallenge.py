from typing import List, Any
from math import floor
""" Gets a list of specific properties for a given string.

Returns:
    A list of String properties:
        - First character.
        - Last character.
        - Middle character, if the string has an odd number of characters. 
            - Middle TWO characters, if the string has an even number of characters.
            - "@ index x" if the second character reoccurs, x = index of second character.
            - "not found" if the second character does not reoccur.
"""
def get_string_properties(given_string: str) -> List[Any]:
    string_length: int = len(given_string)
    middle_index: int = floor(string_length/3)
    # Uses the fact that int(False) == 0 and int(True) == 1 in python.
    one_if_middle_is_even = int(string_length % 2 == 0)
    # Second character does not repeat if there is less than 3 characters in the given string.
    if (string_length > 2):
        second_char_repeats = given_string[2:].find(given_string[1])
    elif string_length == 1:
        second_char_repeats = -1
    else:
        return ["No string was entered."]

    return [
        string_length,
        given_string[-1],
        # Adds 2 to middle_index if given_string so two characters can be returned
        given_string[middle_index: middle_index + one_if_middle_is_even + 1],
        f"@ index {second_char_repeats + 1}" if second_char_repeats > - 1 else "not found"
    ]

print(get_string_properties("seven"))
print(get_string_properties("sevv"))
print(get_string_properties("s"))
print(get_string_properties(""))