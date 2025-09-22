import heapq

def solution(data, queries):
    """
    Process a series of queries on a min-heap.
    
    Supported operations:
    - ["delete", k]: delete the k-th smallest element
    - ["find"]: return the 3rd smallest element in the heap
    
    Args:
        data (list[int]): Initial list of numbers
        queries (list[list]): Queries to process
    
    Returns:
        list[int]: Results of all 'find' queries. If fewer than 3 elements exist,
                   returns -1 for that query.
    """
    heapq.heapify(data)  # ensure input list is a valid heap
    output = []

    for query in queries:
        op = query[0]

        if op == "delete":
            k = query[1]
            temp = []
            # temporarily remove the first (k-1) elements
            for _ in range(k - 1):
                if data:
                    temp.append(heapq.heappop(data))
            # remove the k-th smallest element
            if data:
                heapq.heappop(data)
            # restore the other elements
            for val in temp:
                heapq.heappush(data, val)

        elif op == "find":
            if len(data) >= 3:
                temp = []
                # remove first two elements
                for _ in range(2):
                    temp.append(heapq.heappop(data))
                # get the 3rd smallest
                third_min = heapq.heappop(data)
                output.append(third_min)
                # restore heap
                heapq.heappush(data, third_min)
                for val in temp:
                    heapq.heappush(data, val)
            else:
                output.append(-1)

    return output


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    queries = [["delete", 1], ["find"], ["delete", 2], ["find"]]
    result = solution(data, queries)
    print("Results of 'find' queries:", result)  # [4, 5]
