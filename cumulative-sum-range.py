def solution(arr: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    """
    Precompute maximum subarray sums for every range [i, j] and
    answer queries in O(1) time.

    Args:
        arr (List[int]): The input array of integers.
        queries (List[Tuple[int, int]]): List of queries where each
            query is a tuple (start, end) representing a subarray range.

    Returns:
        List[int]: List of maximum subarray sums for each query.
    """
    n = len(arr)

    # Precompute prefix sums for fast subarray sum calculation
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    # Precompute best[i][j] = max subarray sum for range [i..j]
    best = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            sub_sum = prefix[j + 1] - prefix[i]
            if j == i:
                best[i][j] = sub_sum
            else:
                best[i][j] = max(best[i][j - 1], sub_sum)

    # Answer queries
    return [best[start][end] for start, end in queries]


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
