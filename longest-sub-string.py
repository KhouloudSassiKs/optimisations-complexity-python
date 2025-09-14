"""
Find the length of the longest substring in `s` 
that contains at most `K` distinct characters.

Args:
    s (str): The input string.
    K (int): Maximum number of distinct characters allowed.

Returns:
    int: Length of the longest valid substring.
"""
def solution(s, K):
    if not s:
        return 0

    output = currentsubstring = s[0]
    left, right = 0, 1
    currentLettercount = 1

    while right < len(s):
        if s[right] in currentsubstring:
            currentsubstring += s[right]
            right += 1
        else:
            if currentLettercount < K:
                currentsubstring += s[right]
                currentLettercount += 1
                right += 1
            elif currentLettercount == K:
                removed = s[left]
                left += 1
                currentsubstring = currentsubstring[1:]
                if removed not in currentsubstring:
                    currentsubstring += s[right]
                    right += 1

        if len(currentsubstring) > len(output):
            output = currentsubstring

    return len(output)


if __name__ == "__main__":
    # Example test cases
    print(solution("abcba", 2))   # Expected 3 ("bcb")
    print(solution("aa", 1))      # Expected 2 ("aa")
    print(solution("eceba", 2))   # Expected 3 ("ece")
