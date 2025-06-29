'''
Contains the function to process queries and count occurrences of 'ABC'.
'''
from typing import List, Tuple
def process_queries(S: str, queries: List[Tuple[int, str]]) -> List[int]:
    results = []
    for index, char in queries:
        # Ensure the index is within the valid range and char is a single character
        if 1 <= index <= len(S) and len(char) == 1:
            S = S[:index - 1] + char + S[index:]  # Replace character at the specified index
        # Count occurrences of 'ABC' after modification
        results.append(count_abc(S))  
    return results
def count_abc(S: str) -> int:
    '''
    Counts the occurrences of the substring 'ABC' in the given string S.
    '''
    return sum(1 for i in range(len(S) - 2) if S[i:i + 3] == "ABC")