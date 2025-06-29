'''
Main entry point of the Reel Matcher application.
'''
from reel_matcher import minimum_seconds_to_match_reels
def main():
    try:
        n = int(input("Enter number of reels (N): "))
        if n <= 0:
            raise ValueError("Number of reels must be a positive integer.")
        reels = []
        for i in range(n):
            reel = input(f"Enter reel {i + 1} (must be a string of length 10): ")
            if len(reel) != 10:
                raise ValueError("Each reel must be a string of length 10.")
            reels.append(reel)
        min_time = minimum_seconds_to_match_reels(n, reels)
        print(f"Minimum Time: {min_time} seconds")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Calculation Error: {e}")
if __name__ == "__main__":
    main()