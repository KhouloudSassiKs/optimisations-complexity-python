"""
Find the maximum sum of any contiguous subarray of size k using
the sliding window approach.

Args:
    numbers (list[int]): List of integers.
    k (int): Size of the subarray.

Returns:
    tuple[int, int]: (maximum sum, starting index of that subarray)
"""
def maximum_sum(numbers: list[int], k: int) -> tuple[int, int]:
    length = len(numbers)
    if length < k or k <= 0:
        raise ValueError("Subarray size k must be positive and <= length of numbers")

    # Initialize sliding window
    left = 0
    right = k - 1
    local_sum = sum(numbers[left:right + 1])
    best_sum = local_sum
    best_index = left

    # Slide the window across the array
    while right + 1 < length:
        local_sum = local_sum + numbers[right + 1] - numbers[left]
        left += 1
        right += 1
        if local_sum > best_sum:
            best_sum = local_sum
            best_index = left

    return best_sum, best_index


if __name__ == "__main__":
    print(maximum_sum([1, 2, 3, 4, 5], 2))     # (9, 3) → subarray [4,5]
    print(maximum_sum([-1, -2, -3, -4], 2))    # (-3, 0) → subarray [-1,-2]
    print(maximum_sum([5, -1, 2, 10, -2], 3))  # (11, 1) → subarray [-1,2,10]
