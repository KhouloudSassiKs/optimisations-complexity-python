def solution(arr):
    """
    Count the total number of pairs in the array.
    A pair is defined as two identical elements.

    Args:
        arr (list[int]): Input array of integers.

    Returns:
        int: Total number of pairs.
    """
    count = 0
    countdict = {}
    
    # Count occurrences of each element
    arr.sort()  # optional for counting, but keeping as in original
    for number in arr:
        countdict[number] = countdict.get(number, 0) + 1

    # Calculate pairs for each element
    for v in countdict.values():
        count += v * (v - 1) // 2  # integer division

    return count


if __name__ == "__main__":
    arr = [1, 1, 1, 2, 2, 4, 5, 5]
    print(f"Array: {arr}")
    print(f"Total pairs: {solution(arr)}")
