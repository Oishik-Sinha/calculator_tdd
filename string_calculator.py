def add(numbers: str) -> int:
    if not numbers:
        return 0
    if "," not in numbers:
        return int(numbers)