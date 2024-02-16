from collections.abc import Iterable


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers,
    return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)

def test_sum_even_numbers(numbers: Iterable[int]) -> int:
    
    assert sum_even_numbers([2,4]) == 3
