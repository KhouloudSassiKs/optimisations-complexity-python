from sortedcontainers import SortedList

def solution(operations):
    """
    Implements a dynamic ordered set with three supported operations:

    Operations:
        [0, x] -> Insert x (if not already present), then output current size
        [1, x] -> Remove x (if present), then output current size
        [2]    -> Output maximum element in the set (or -1 if empty)

    Args:
        operations (list[list[int]]): List of operations to perform.

    Returns:
        list[int]: Results from each operation.
    """
    myset = SortedList()
    output = []

    for op in operations:
        if op[0] == 0:  # Insert operation
            number = op[1]
            if number not in myset:
                myset.add(number)
            output.append(len(myset))

        elif op[0] == 1:  # Remove operation
            number = op[1]
            myset.discard(number)  # safe remove
            output.append(len(myset))

        elif op[0] == 2:  # Max query
            if myset:
                output.append(myset[-1])
            else:
                output.append(-1)

    return output


# -------------------
# Example usage
# -------------------
if __name__ == "__main__":
    ops = [
        [0, 5],   # insert 5 -> size = 1
        [0, 3],   # insert 3 -> size = 2
        [2],      # max -> 5
        [1, 5],   # remove 5 -> size = 1
        [2],      # max -> 3
        [1, 10],  # remove 10 (not present) -> size = 1
        [2],      # max -> 3
    ]
    print(solution(ops))  # [1, 2, 5, 1, 3, 1, 3]
