from collections.abc import Iterable


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, 
    return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)

if __name__ == "__main__":
  print(sum_even_numbers(1234))
