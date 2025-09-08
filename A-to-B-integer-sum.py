"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Returns the sum of all integers between a and b inclusive.
Works regardless of the order of a and b.
"""
def solution(a, b):
    if a == b:
        return a
    
    small, big = min(a, b), max(a, b)
    return ((big - small + 1) * (big + small)) // 2


# Examples
print(solution(123, 321))  # Output: 44178
print(solution(5, 1))      # Output: 15  (1+2+3+4+5)
print(solution(7, 7))      # Output: 7
print(solution(-2, 2))     # Output: 0  (-2 + -1 + 0 + 1 + 2)
