import heapq

def solution(operations):
    """
    Implements a max-heap that supports three operations:
    - "Add": insert a number
    - "Max": record the current maximum value
    - "RemoveMax": remove the current maximum value

    Args:
        operations (list[tuple[str, int]]): List of operations, each represented as (operation, number).
            Example: [("Add", 5), ("Max", 0), ("RemoveMax", 0)]

    Returns:
        list[int]: A list of maximum values recorded during "Max" operations.
    """
    my_heap = []       # Python heapq is a min-heap, so we push negative values
    maximum_values = []  # Stores results of "Max" operations

    for op, number in operations:
        if op == "Add":
            heapq.heappush(my_heap, -number)  # negate for max-heap behavior
        elif op == "Max" and my_heap:
            maximum_values.append(-my_heap[0])  # peek the max
        elif op == "RemoveMax" and my_heap:
            heapq.heappop(my_heap)  # remove the max element

    return maximum_values

if __name__ == "__main__":
    ops = [
        ("Add", 5),
        ("Add", 10),
        ("Max", 0),       # should capture 10
        ("RemoveMax", 0),
        ("Max", 0),       # should capture 5
        ("Add", 7),
        ("Max", 0),       # should capture 7
    ]

    result = solution(ops)
    print("Results of Max operations:", result)  # [10, 5, 7]
