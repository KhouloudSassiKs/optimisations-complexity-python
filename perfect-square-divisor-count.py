import bisect
import math
from typing import List


def solution(arr):
    """
    For each number in `arr`, find the closest perfect square and return
    the number of divisors of that square.

    Args:
        arr (List[int]): Input list of integers.

    Returns:
        List[int]: List where each element is the divisor count of the
                   closest perfect square to the corresponding number.
    """
    # Precompute perfect squares up to a safe limit
    squares = [i * i for i in range(1, 10000)]

    output = []
    for number in arr:
        closest = find_closest_square(squares, number)
        output.append(count_divisors(closest))

    return output


def find_closest_square(squares: List[int], number: int) -> int:
    """
    Find the closest perfect square to a given number using binary search.

    Args:
        squares (List[int]): Precomputed list of squares.
        number (int): The target number.

    Returns:
        int: The closest perfect square.
    """
    if number in squares:
        return number

    insertion_index = bisect.bisect_left(squares, number)

    if insertion_index == 0:
        return squares[0]
    if insertion_index == len(squares):
        return squares[-1]

    before = squares[insertion_index - 1]
    after = squares[insertion_index]

    return before if abs(before - number) <= abs(after - number) else after


def count_divisors(number: int) -> int:
    """
    Count the number of divisors of a given integer efficiently.

    Args:
        number (int): Input number.

    Returns:
        int: Count of divisors.
    """
    count = 0
    root = int(math.isqrt(number))

    for i in range(1, root + 1):
        if number % i == 0:
            count += 1  # i is a divisor
            if i != number // i:
                count += 1  # add the pair divisor

    return count


if __name__ == "__main__":
    # Example usage
    arr = [10, 20, 50]
    print("Input:", arr)
    print("Output (divisor counts of closest squares):", solution(arr))
