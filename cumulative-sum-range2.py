from typing import List, Tuple


def solution(arr: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    """
    For each query (start, end), return the maximum subarray sum
    for all subarrays that begin at `start` and end anywhere up to `end`.

    Args:
        arr (List[int]): The input array of integers.
        queries (List[Tuple[int, int]]): List of queries, where each query
            is a tuple (start, end) representing a subarray range.

    Returns:
        List[int]: A list of maximum subarray sums, one per query.
    """
    # Precompute prefix sums for each starting index
    precalc = {}
    for i in range(len(arr)):
        current_sum = 0
        sums_from_i = []
        for number in arr[i:]:
            current_sum += number
            sums_from_i.append(current_sum)
        precalc[i] = sums_from_i

    # Answer queries
    output = []
    for start, end in queries:
        if start == end:
            output.append(arr[start])
        else:
            possible_sums = precalc[start][: end - start + 1]
            output.append(max(possible_sums))
    return output


if __name__ == "__main__":
    # Example 1
    arr1 = [1, 2, 3]
    queries1 = [(0, 2), (1, 2), (0, 1)]
    print("Example 1:", solution(arr1, queries1))
    # Expected: [6, 5, 3]

    # Example 2
    arr2 = [2, -1, 4, -2, 1]
    queries2 = [(0, 2), (1, 3), (2, 4)]
    print("Example 2:", solution(arr2, queries2))
    # Expected: [5, 4, 4]

    # Example 3
    arr3 = [5, -3, 2, 7, -1]
    queries3 = [(0, 4), (0, 1), (2, 3)]
    print("Example 3:", solution(arr3, queries3))
    # Expected: [11, 5, 9]
