"""
Compute the largest gap between consecutive occurrences of words in a list.

Args:
    word_list (list[str]): List of words.

Returns:
    dict[str, int]: Dictionary mapping each word to the largest distance
    between consecutive occurrences.
    
Example:
    solution(["apple", "banana", "apple", "apple", "banana"])
    ->    {'apple': 2, 'banana': 3}
"""
def solution(word_list: list[str]) -> dict[str, int]:
    output = {}
    first_occurrence = {}
    last_occurrence = {}

    for index, word in enumerate(word_list):
        if word not in first_occurrence:
            first_occurrence[word] = index
        else:
            if word in last_occurrence:
                # Compare distance from previous last_occurrence vs current index
                if last_occurrence[word] - first_occurrence[word] >= index - last_occurrence[word]:
                    first_occurrence[word] = last_occurrence[word]
                    last_occurrence[word] = index
            else:
                last_occurrence[word] = index

            # Update output with the current largest distance
            output[word] = last_occurrence.get(word, index) - first_occurrence[word]

    return output


if __name__ == "__main__":
    words = ["apple", "banana", "apple", "apple", "banana"]
    print(solution(words))
    # Expected output: {'apple': 2, 'banana': 3}

    words2 = ["cat", "dog", "cat", "mouse", "cat", "dog"]
    print(solution(words2))
    # Expected output: {'cat': 3, 'dog': 4}
