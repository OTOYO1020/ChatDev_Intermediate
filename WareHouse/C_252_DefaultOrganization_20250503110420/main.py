'''
Main application file for the reel symbol matching program.
'''
from reel_manager import ReelManager
def main():
    '''
    Main function to run the reel symbol matching logic.
    '''
    try:
        num_reels = int(input("Enter number of reels: "))
        symbols = []
        for _ in range(num_reels):
            symbol = input("Enter symbols for each reel (10 characters long): ")
            if len(symbol) != 10:
                raise ValueError("Each symbol must be exactly 10 characters long.")
            symbols.append(symbol)
        if num_reels < 2:
            raise ValueError("Invalid input. Ensure there are at least 2 reels.")
        reel_manager = ReelManager(num_reels)
        reel_manager.add_symbols(symbols)
        min_time = reel_manager.calculate_min_time()
        if min_time is not None:
            print(f"Minimum time: {min_time}")
        else:
            print("Impossible to match symbols.")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()