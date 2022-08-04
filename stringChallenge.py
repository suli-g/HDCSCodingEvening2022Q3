""" Gets a list of specific properties for a given string.

Returns:
    A list of properties
"""
from typing import List, Any

def get_string_properties(given_string: str) -> List[Any]:
    string_length: int = len(given_string)
    middle_index: int = round(string_length/2)
    repeat_index: int = given_string.index(given_string[1])
    result: List[Any] = []
    result.append(string_length)
    result.append(given_string[-1])
    result.append(given_string[middle_index])
    if middle_index % 2 != 0:
        result.append(given_string[middle_index - 1] + given_string[middle_index])
    else:
        result.append(given_string[middle_index])
    result.append(f"@ index {repeat_index}" if repeat_index > - 1 else "not found")
    return result

print(get_string_properties("sevven"))