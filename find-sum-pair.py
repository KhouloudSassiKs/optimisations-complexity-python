"""
Find a pair of numbers in `arr` whose sum equals `target`.

Args:
     arr (List[int]): List of integers to search within.
     target (int): The target sum to find.

Returns:
     List[int]: A pair of numbers [a, b] that sum to `target`, or
     an empty list if no such pair exists.
"""
def solution(arr, target):
    seen = {}
    for number in arr:
        remaining = target - number
        if remaining in seen:
            return [remaining, number]
        seen[number] = True
    return []
