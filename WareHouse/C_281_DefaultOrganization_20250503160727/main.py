'''
Main application file to run the playlist duration calculator.
'''
def main():
    # Read integers N and T from standard input
    N, T = map(int, input().split())
    # Read an array A of length N, which contains the durations of each song in seconds
    A = list(map(int, input().split()))
    # Calculate the total duration of the playlist
    total_duration = sum(A)
    # Check for edge case where total_duration is zero
    if total_duration == 0:
        print("Total duration of the playlist is zero. No songs to play.")
        return
    # Compute the effective time
    effective_time = T % total_duration
    elapsed_time = 0
    current_song = -1
    seconds_passed = 0
    # Iterate through each song in the playlist
    for i in range(N):
        elapsed_time += A[i]
        if elapsed_time >= effective_time:  # Change from '>' to '>='
            current_song = i + 1  # 1-based index
            # Calculate seconds passed since the start of the current song
            seconds_passed = effective_time - (elapsed_time - A[i])
            break
    # Print the current song number and seconds passed since it started playing
    if current_song == -1:
        print("No song is currently playing.")
    else:
        print(f"Current Song: {current_song}, Seconds Passed: {seconds_passed}")
if __name__ == "__main__":
    main()