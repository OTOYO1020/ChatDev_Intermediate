def match_phrase(song_notes, phrase_sounds):
    '''
    This function takes in two sequences of non-negative integers and finds the number of integers i that satisfy 1 ≤ i ≤ N - M + 1 and meet the condition.
    Parameters:
    - song_notes (str): A string representing the sequence of song notes.
    - phrase_sounds (str): A string representing the sequence of phrase sounds.
    Returns:
    - count (int): The number of integers i that satisfy the condition.
    '''
    # Convert the song notes and phrase sounds to lists of integers
    song_notes = list(map(int, song_notes.split()))
    phrase_sounds = list(map(int, phrase_sounds.split()))
    n = len(song_notes)
    m = len(phrase_sounds)
    count = 0
    # Iterate through all possible starting positions of the phrase in the song
    for i in range(n - m + 1):
        # Get the subsequence of song notes of length m starting from position i
        subsequence = song_notes[i:i+m]
        # Check if the subsequence matches the phrase sounds
        if subsequence == phrase_sounds:
            count += 1
    return count