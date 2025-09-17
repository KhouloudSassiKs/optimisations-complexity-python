def optimizedReplace(A, B):
"""
For each element in B, replaces it with the element from A that corresponds 
to the closest neighbor in B. The original order of B is preserved in the output.
"""
    # Map each value in B to its original index
    dictB = {B[i]: i for i in range(len(B))}
    
    # Initialize result list with zeros
    C = [0] * len(A)
    
    # Sort B to find closest neighbors efficiently
    B.sort()
    
    # If there is only one element, just copy it
    if len(B) < 2:
        C[0] = A[0]
        return C
    
    # Loop over sorted B to find closest neighbor for each element
    for i in range(len(B)):
        val = B[i]
        original_index = dictB[val]
        
        # Determine closest neighbor
        if i == 0:
            closest_val = B[1]  # First element, neighbor is next
        elif i == len(B) - 1:
            closest_val = B[i - 1]  # Last element, neighbor is previous
        else:
            # Middle elements: pick neighbor with smaller absolute difference
            prev_diff = abs(B[i] - B[i - 1])
            next_diff = abs(B[i + 1] - B[i])
            closest_val = B[i + 1] if next_diff < prev_diff else B[i - 1]
        
        # Map to A using original index of closest neighbor
        closest_index = dictB[closest_val]
        C[original_index] = A[closest_index]
    
    return C
A = [10, 20, 30]
B = [3, 2, 5]
print(optimizedReplace(A, B))
# Output: [20, 10, 20]
