"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Returns the minimum absolute difference among all pairs in the list.
If the list has fewer than 2 elements, returns 0.
"""
def solution(nums):
    if len(nums) < 2:
        return 0

    # Sort the list to compare adjacent elements
    nums.sort()

    # Compute minimum absolute difference between consecutive elements
    best_min = min(abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1))

    return best_min

# Example 1: Normal list of integers
nums = [5, 2, 9, 1, 7]
print(solution(nums))  
# Output: 1  (difference between 1 and 2)

# Example 2: List with negative numbers
nums = [-10, -3, 0, 2, 5]
print(solution(nums))  
# Output: 2  (difference between 0 and 2)

# Example 3: List with duplicate elements
nums = [4, 2, 7, 4, 10]
print(solution(nums))  
# Output: 0  (difference between 4 and 4)

# Example 4: List with a single element
nums = [5]
print(solution(nums))  
# Output: 0  (fewer than 2 elements)

# Example 5: Already sorted list
nums = [1, 3, 6, 10]
print(solution(nums))  
# Output: 2  (difference between 1 and 3)
