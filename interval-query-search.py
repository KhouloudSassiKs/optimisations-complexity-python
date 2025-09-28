from sortedcontainers import SortedList
from typing import List, Tuple


def solution(intervals: List[List[int]], queries: List[List[int]]) -> List[bool | int]:
    """
    Process interval queries on a SortedList of intervals.

    Queries:
        - [0, x, y]: check if [x, y] overlaps with any interval.
                     Returns True or False.
        - [1, x, y]: remove [x, y] from the intervals (if present)
                     and return the updated count of intervals.

    Args:
        intervals (List[List[int]]): Initial intervals, each [start, end].
        queries (List[List[int]]): Queries to process.

    Returns:
        List[bool | int]: Results corresponding to the queries.
    """
    # convert input intervals into tuples for consistency
    sl = SortedList(map(tuple, intervals))
    output: List[bool | int] = []

    for query in queries:
        operation, *query_interval = query
        query_tuple: Tuple[int, int] = tuple(query_interval)

        if operation == 0:  # overlap check
            x, y = query_tuple
            found = False

            idx = sl.bisect_left(query_tuple)

            # Only need to check the interval at idx and the one before it
            if idx < len(sl) and y >= sl[idx][0] and x <= sl[idx][1]:
                found = True
            elif idx > 0 and y >= sl[idx - 1][0] and x <= sl[idx - 1][1]:
                found = True

            output.append(found)

        elif operation == 1:  # removal
            if query_tuple in sl:
                sl.remove(query_tuple)
            output.append(len(sl))

    return output


if __name__ == "__main__":
    intervals = [[1, 10], [5, 15], [20, 30]]
    queries = [
        [0, 6, 9],    # overlaps with (1,10) and (5,15)
        [0, 21, 29],  # overlaps with (20,30)
        [0, 11, 19],  # no overlap
        [1, 5, 15],   # remove (5,15)
        [0, 6, 9],    # still overlaps with (1,10)
    ]

    print(solution(intervals, queries))
    # Expected: [True, True, False, 2, True]
