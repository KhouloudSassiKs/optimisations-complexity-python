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
    unique_words = set(s.split())
    processed_letters = set()
    max_letter = s[0]
    max_count = 0

    for letter in s.strip():
        if letter in processed_letters:
            continue
        processed_letters.add(letter)

        count = sum(1 for word in unique_words if letter in word)
        if count > max_count:
            max_count = count
            max_letter = letter

    return (max_letter, max_count)


if __name__ == "__main__":
    print(solution("tiger cheetah lion"))           # ('t', 2)
    print(solution("elephant eagle emu"))           # ('e', 3)
    print(solution("zebra antelope gorilla"))       # ('a', 3)
    print(solution("apple apricot banana avocado")) # ('a', 4)


