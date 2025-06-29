'''
Main application file for the Song Player.
'''
from song_logic import find_current_song_and_time
def main():
    '''
    Main function to run the song player logic without GUI.
    '''
    try:
        N = int(input("Enter number of songs (N): "))
        A = list(map(int, input("Enter song durations (A) separated by space: ").split()))
        T = int(input("Enter total time (T): "))
        if len(A) != N:
            raise ValueError("The number of durations must match N.")
        song_index, elapsed_time = find_current_song_and_time(N, A, T)
        print(f"Current Song Index: {song_index}, Elapsed Time: {elapsed_time} seconds")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()