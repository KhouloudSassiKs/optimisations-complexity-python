"""
Find the letter that appears in the most unique words
from the given string.

Args:
    s (str): Input string containing words.
Returns:
    tuple(str, int): The letter and the number of unique words it appears in.

Example:
        solution("tiger cheetah lion") -> ('t', 2)
"""
def solution(s: str) -> tuple[str, int]:
    words = set(s.split())
    max_letter = None
    max_count = 0

    # Check only unique letters (ignore spaces)
    for letter in set(s.replace(" ", "")):
        count = sum(1 for word in words if letter in word)
        if count > max_count:
            max_count = count
            max_letter = letter

    return (max_letter, max_count)


if __name__ == "__main__":
    # Example runs
    print(solution("tiger cheetah lion"))
    # Expected: ('t', 2) → 't' appears in "tiger" and "cheetah"

    print(solution("elephant eagle emu"))
    # Expected: ('e', 3) → 'e' appears in all three words

    print(solution("zebra antelope gorilla"))
    # Expected: ('a', 3) → 'a' appears in all three words
