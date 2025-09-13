"""
Partition a string into the smallest possible substrings
such that no character appears in more than one substring.

Args:
    s (str): Input string.

Returns:
    list[int]: A list of partition lengths.

Example:
    string_partition("abacdcd")    -> [3, 4]
"""
def string_partition(s: str) -> list[int]:
    # record last occurrence of each character
    last_pos = {letter: index for index, letter in enumerate(s)}

    output = []
    start_substring = 0
    end_substring = 0

    # expand partitions until we reach the last occurrence
    for index, letter in enumerate(s):
        end_substring = max(end_substring, last_pos[letter])
        if index == end_substring:
            output.append(end_substring - start_substring + 1)
            start_substring = index + 1

    return output


if __name__ == "__main__":
    # Example runs
    print(string_partition("abacdcd"))              # [3, 4] → "aba", "cdcd"
    print(string_partition("eccbbbbdec"))           # [10]   → whole string
    print(string_partition("ababcbacadefegdehijhklij"))  # [9, 7, 8]
