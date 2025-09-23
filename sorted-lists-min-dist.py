from sortedcontainers import SortedList

def solution(queries):
    """
    For each prefix of queries, return the smallest distance between 
    any two numbers in the set so far. If only one element exists, return -1.
    """
    sorted_list = SortedList()
    output = []
    min_dist = float("inf")

    for num in queries:
        sorted_list.add(num)

        if len(sorted_list) == 1:
            # Only one number so far
            output.append(-1)
        else:
            # Find neighbors of current number
            idx = sorted_list.bisect_left(num)

            if idx > 0:  # left neighbor exists
                min_dist = min(min_dist, num - sorted_list[idx - 1])
            if idx < len(sorted_list) - 1:  # right neighbor exists
                min_dist = min(min_dist, sorted_list[idx + 1] - num)

            output.append(min_dist)

    return output


# -------------------
# Example usage
# -------------------
if __name__ == "__main__":
    queries = [3, 9, 5, 1, 8]
    print(solution(queries))  # [-1, 6, 2, 2, 1]
