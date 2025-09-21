def solution(arr: list[int]) -> int:
    """
    Count the number of pairs (i, j) such that |arr[i] - arr[j]| >= 10.

    Args:
        arr (list[int]): Input list of integers.

    Returns:
        int: The number of valid pairs.
    """
    arr.sort()
    n = len(arr)
    count = 0
    j = 0

    for i in range(n):
        # Move j until the difference is greater than 10
        while j < n and arr[j] - arr[i] <= 10:
            j += 1
        # All elements from j..n-1 form valid pairs with i
        count += n - j

    return count


if __name__ == "__main__":
    # Example usage
    arr = [1, 5, 12, 20, 25]
    print(solution(arr))  # Expected output: 7
