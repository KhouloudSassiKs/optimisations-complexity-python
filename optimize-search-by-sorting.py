"""
Find all unique pairs of integers in the list that sum to zero.

Uses the two-pointer approach on a sorted list to efficiently
find pairs. Returns the pairs sorted from smallest to largest.

Args:
    input_list (list[int]): List of integers.

Returns:
    list[tuple[int, int]]: Sorted list of pairs that sum to zero.
"""
def find_neutral_pair(input_list):
    output = []
    sorted_list = sorted(input_list)
    left, right = 0, len(sorted_list) - 1

    while left < right:
        total = sorted_list[left] + sorted_list[right]

        if total == 0:
            output.append((sorted_list[left], sorted_list[right]))
            left += 1
            right -= 1
        elif total < 0:
            left += 1  # need a larger number
        else:
            right -= 1  # need a smaller number

    return sorted(output)


if __name__ == "__main__":
    print(find_neutral_pair([3, -3, 2, -2, 5, -5, 1]))
    # [(-5, 5), (-3, 3), (-2, 2)]

    print(find_neutral_pair([4, -1, -4, 1, 2, -2, 3]))
    # [(-4, 4), (-2, 2), (-1, 1)]

    print(find_neutral_pair([10, -10, 5, -3, 3, 7]))
    # [(-10, 10), (-3, 3)]
