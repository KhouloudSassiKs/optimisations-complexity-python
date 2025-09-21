def solution(s):
    """
    Count the total number of 3-letter combinations from the string `s`
    where exactly two letters are identical and the third is different.

    Args:
        s (str): Input string.

    Returns:
        int: Total number of valid 3-letter combinations.
    """
    # Count occurrences of each letter
    letter_count = {}
    for letter in s:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    letters = list(letter_count.keys())
    output = 0

    # Loop over all pairs of distinct letters
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            a, b = letters[i], letters[j]
            count_a, count_b = letter_count[a], letter_count[b]

            # Two a's + one b
            if count_a >= 2:
                output += (count_a * (count_a - 1) // 2) * count_b
            # Two b's + one a
            if count_b >= 2:
                output += (count_b * (count_b - 1) // 2) * count_a

    return output


if __name__ == "__main__":
    test_strings = ["aabc", "aaab", "abcd", "aabbcc"]
    for s in test_strings:
        print(f"String: {s} -> Total combinations: {solution(s)}")
