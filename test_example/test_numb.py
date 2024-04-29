
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from numb import sum_even_numbers


def test_sum_even_numbers():
    numbers = [2, 4]
    assert sum_even_numbers(numbers) == 6
