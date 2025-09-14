from collections import defaultdict
"""
Find the influencer node in a network of connections. 
Influence is measured as the sum of a node's direct connections 
plus the connections of its neighbors. In case of a tie, 
the smallest node is returned.

Args:
    connections (list[tuple[int, int]]): List of (A, B) connections.

Returns:
    nt: Node with the highest influence.
"""
def find_influencer(connections):
    directconnection = defaultdict(set)
    nestedconnection = defaultdict(set)
    allConnection = {}

    # Build direct connections
    for A, B in connections:
        directconnection[A].add(B) 
        directconnection[B].add(A)  # Treat as undirected

    # Build nested connections (connections of neighbors)
    for item, setConnection in directconnection.items():
        for nest in setConnection:
            nestedconnection[item] |= directconnection[nest]

    # Compute total connections
    for item, setConnection in directconnection.items():
        allConnection[item] = len(setConnection) + len(nestedconnection[item])

    # Find node with maximum connections; break ties by smallest key
    maxval = max(allConnection.values())
    minKey = min(k for k, v in allConnection.items() if v == maxval)

    return minKey


if __name__ == "__main__":
    connections = [(1, 2), (2, 3), (3, 4), (4, 5)]
    print(find_influencer(connections))  # Example output: 3
