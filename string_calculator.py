def add(numbers: str) -> int:
    if not numbers:
        return 0
    tokens = [numbers]
    if "," in numbers:
        tokens = numbers.split(",")
    return sum(int(t) for t in tokens)