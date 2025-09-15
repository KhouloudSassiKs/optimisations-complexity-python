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
     
if __name__ == "__main__":
    # Example 1: simple case
    arr = [2, 7, 11, 15]
    target = 9
    print("Example 1:", solution(arr, target))  # Output: [2, 7]

    # Example 2: no pair exists
    arr = [1, 2, 3, 4]
    target = 8
    print("Example 2:", solution(arr, target))  # Output: []

    # Example 3: negative numbers
    arr = [-3, 4, 1, 2]
    target = 1
    print("Example 3:", solution(arr, target))  # Output: [-3, 4]

    # Example 4: multiple possible pairs (returns first found)
    arr = [1, 3, 2, 2, 4]
    target = 4
    print("Example 4:", solution(arr, target))  # Output: [2, 2] or [1, 3]
