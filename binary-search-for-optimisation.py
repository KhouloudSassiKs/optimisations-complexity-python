"""
For each element in Y, find the element in X whose value is 
closest to half of that Y element, and return the corresponding 
Y element at the original index.

Args:
    X (list[int]): List of integers.
    Y (list[int]): List of integers.

Returns:
    list[int]: List of Y elements corresponding to closest X values.
"""
def solution(X, Y):
    output = []
    # Map each value in X to its index
    xindexes = {X[i]: i for i in range(len(X))}
    sortedArray = sorted(X)

    for y in Y:
        closestx = find_closest(y / 2, sortedArray, xindexes)
        output.append(Y[closestx])

    return output

 """
Find the index of the value in 'array' closest to 'y' using binary search.

Args:
     y (float): Target value to find closest to.
     array (list[int]): Sorted list of integers.
     indexdict (dict[int, int]): Mapping from array value to original index in X.

Returns:
     int: Index of the closest value in the original X list.
 """
def find_closest(y, array, indexdict):
    left, right = 0, len(array) - 1
    closest = array[0]

    while left <= right:
        middle = (left + right) // 2
        current = array[middle]

        # Update closest if this element is nearer
        if abs(y - current) < abs(y - closest):
            closest = current

        if current == y:
            return indexdict[current]
        elif current < y:
            left = middle + 1
        else:
            right = middle - 1

    return indexdict[closest]


if __name__ == "__main__":
    X = [10, 20, 30, 40]
    Y = [35, 70, 25]

    print(solution(X, Y))
    # Example output: [35, 70, 25] (depending on input values)
