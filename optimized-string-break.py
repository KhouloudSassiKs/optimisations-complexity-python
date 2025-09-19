def solution(S, Q):
    """
    For each query (letter1, letter2), remove occurrences of these two letters 
    from the string S and return the length of the longest contiguous substring 
    that remains.

    Args:
        S (str): The input string.
        Q (List[Tuple[str, str]]): A list of queries, where each query is a tuple 
                                   of two letters to remove.

    Returns:
        List[int]: A list of integers where each element is the maximum substring 
                   length after processing the corresponding query.

    Examples:
        >>> solution("aabbbaaaccab", [("a", "b"), ("c", "a")])
        [2, 3]

        >>> solution("xyzxyz", [("x", "y"), ("z", "x")])
        [2, 2]

        >>> solution("aaaa", [("a", "b")])
        [0]
    """
    output = []
    
    for letter1, letter2 in Q:
        # Replace target letters with spaces
        processed = S.replace(letter1, " ").replace(letter2, " ")
        # Split by spaces to get substrings
        substrings = processed.split()
        # Get lengths of substrings
        lengths = [len(substring) for substring in substrings]
        # Append max length or 0 if no substrings exist
        output.append(max(lengths, default=0))

    return output


if __name__ == "__main__":
    # Example usage
    S = "aabbbaaaccab"
    Q = [("a", "b"), ("c", "a")]
    print(solution(S, Q))  # [2, 3]
