from typing import List, Any

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
    middle_index: int = int(string_length/2)
    second_char_repeats = given_string[2:].find(given_string[1])

    return [
        string_length,
        given_string[-1],
        # Uses the fact that int(False) == 0 and int(True) == 1 in python.
        given_string[middle_index: middle_index + 1 + int(string_length % 2 != 0)],
        f"@ index {second_char_repeats + 1}" if second_char_repeats > - 1 else "not found"
    ]

print(get_string_properties("seven"))
print(get_string_properties("sevv"))