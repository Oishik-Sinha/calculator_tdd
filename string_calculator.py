import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    delimiter = ",|\n"
    if numbers.startswith("//"):
        delim, numbers = numbers.split("\n", 1)
        delimiter = delim[2:]

    tokens = re.split(delimiter, numbers) 
    return sum(int(t) for t in tokens)  