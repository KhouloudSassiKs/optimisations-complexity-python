"""
Find the longest contiguous subarray whose sum is exactly k.

Args:
     array (list[int]): List of integers.
     k (int): Target sum.

Returns:
     list[int]: The longest contiguous subarray with sum equal to k.
     Returns an empty list if no such subarray exists.
"""
def get_longest_subarray(array: list[int], k: int) -> list[int]:
    if not array:
        return []

    left = right = 0
    current_sum = array[0]
    current_count = 1
    best_count = 0
    output = []

    while right < len(array):
        if current_sum < k:
            right += 1
            if right < len(array):
                current_sum += array[right]
                current_count += 1
        elif current_sum > k:
            current_sum -= array[left]
            left += 1
            current_count -= 1
        else:  # current_sum == k
            if current_count > best_count:
                best_count = current_count
                output = array[left:right + 1]

            # Move the window forward
            current_sum -= array[left]
            left += 1
            current_count -= 1

    return output


if __name__ == "__main__":
    print(get_longest_subarray([1, 2, 3, 4, 2], 6))  # [1, 2, 3]
    print(get_longest_subarray([1, 2, 1, 1, 1, 1], 3))  # [1, 2]
    print(get_longest_subarray([5, -1, 2, 3], 4))  # [5, -1]
    print(get_longest_subarray([1, 2, 3], 10))  # []
