'''
Module for processing votes to find the most voted strings.
'''
from typing import List
def find_most_voted_strings(N: int, votes: List[str]) -> List[str]:
    vote_count = {}
    # Count occurrences of each string
    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1
    # Determine the maximum count of votes
    max_count = max(vote_count.values())
    # Extract strings with the maximum count
    most_voted = [string for string, count in vote_count.items() if count == max_count]
    # Sort the extracted strings in lexicographical order
    most_voted.sort()
    return most_voted