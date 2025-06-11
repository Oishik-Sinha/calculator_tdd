import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    delimiter = ",|\n"
    if numbers.startswith("//"):
        delim, numbers = numbers.split("\n", 1)
        delimiter = delim[2:]

    tokens = re.split(delimiter, numbers) 
    nums = [int(t) for t in tokens]
    neg = [n for n in nums if n < 0]
    if neg:
        raise ValueError("negative numbers not allowed " + ",".join(map(str, neg)))
    return sum(nums)  