import re
from typing import List

def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    delimiter, numbers_str = extract_delimiter_and_numbers(numbers)
    tokens = split(numbers_str, delimiter)
    nums =convert_to_list_of_int(tokens)
    check_negative_values(nums)
    return sum(nums)  

def extract_delimiter_and_numbers(string: str) -> tuple[str, str]:
    """
    Extract the numers and delimiters from the given string if any.\n
    Example : The beginning of the string will contain a separate line that looks like this: "//[delimiter]\n[numbers…]". For example, "//;\n1;2" where the delimiter is ";" should return 3
    """
    if string.startswith("//"):
        header, numbers = string.split("\n", 1)
        custom_delimiter =  header[2:]
        return custom_delimiter, numbers
    return r",|\n", string


def split(s: str, delimiter_pattern: str) -> List[str]:
    """Split the number string using the given delimiter."""
    return re.split(delimiter_pattern, s)


def check_negative_values(numbers: list[int]) -> None:
    """Raises ValueError if any negative numbers are found."""
    negatives = [n for n in numbers if n < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")
    

def convert_to_list_of_int(tokens: List[str]) -> List[int]:
    "Convert the number string in list of integers"
    return [int(t) for t in tokens if t.strip()]
