"""
Return the scores of queried player IDs.

Args:
    player_ids (List[int]): List of player IDs.
    player_scores (List[int]): Corresponding list of player scores.
    queries (List[int]): List of player IDs to query.

Returns:
    List[int]: Scores of the queried player IDs that exist in player_ids.
"""
def solution(player_ids, player_scores, queries):
    # Build a dictionary mapping player ID to score
    id_to_score = dict(zip(player_ids, player_scores))
    
    # Retrieve scores for the queried IDs if they exist
    return [id_to_score[player_id] for player_id in queries if player_id in id_to_score]


if __name__ == "__main__":
    # Example 1
    player_ids = [1, 2, 3, 4, 5]
    player_scores = [100, 200, 150, 50, 300]
    queries = [3, 5, 7]
    print("Example 1:", solution(player_ids, player_scores, queries))  # Output: [150, 300]

    # Realistic test case
    player_ids = [13, 41, 14, 2, 44, 54, 37, 48, 23, 52, 20, 31, 53, 43, 3, 42, 45, 10, 9, 18, 15, 17, 7, 21, 12, 50, 59, 16, 6, 5, 61, 11, 1, 30, 46, 25, 29, 60, 19, 49, 56, 39, 33, 8, 22, 55, 34, 58, 4, 38, 35, 36, 47, 27, 51, 26, 32, 24, 40, 28, 57]
    player_scores = [-116776, 126190, 709753, 197937, -711437, -295807, -921271, -315070, 5820, -194189, -402939, 16780, 906154, 260352, -222304, -625045, 902189, 506928, 412007, 825263, 924499, -273356, -901962, 391263, -394058, 264896, -192884, 466414, -255471, -884129, -320033, -80685, 58827, -630349, 494719, -288459, 751261, 696192, -774397, -14287, -171181, -109872, 342648, 874234, -391002, 153449, 165803, -309312, 346374, 813454, 510659, -533021, 928743, -261481, -485500, -575684, 137762, -371905, 685261, 311109, -996746]
    queries = [38, 55, 60, 36, 51, 17, 18, 42, 30, 5, 61, 46, 31, 13, 45, 15, 16, 40, 26, 29, 59, 48, 35, 52, 27, 24, 41, 11, 34, 57, 28, 39, 1, 7, 47, 33, 6, 56, 44, 53, 32, 58, 54, 14, 10, 9]
    
    expected_result = [813454, 153449, 696192, -533021, -485500, -273356, 825263, -625045, -630349, 751261, -320033, 494719, 16780, -116776, 902189, 924499, 466414, 685261, -575684, 751261, -192884, -315070, 510659, -194189, -261481, -371905, 126190, -80685, 165803, -996746, 311109, -109872, 58827, -901962, 928743, 342648, -255471, -171181, -711437, 906154, 137762, -309312, -295807, 709753, 506928, 412007]

    result = solution(player_ids, player_scores, queries)
    print("Realistic test case passed:", result == expected_result)
