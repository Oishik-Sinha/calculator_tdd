import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    tokens = re.split(",|\n", numbers) 
    return sum(int(t) for t in tokens)  