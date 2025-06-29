'''
Main application file for the Coin Collector.
'''
from typing import List, Tuple
from coin_collector import max_coins, input_validation
def main():
    while True:
        try:
            # Read input values
            H = int(input("Enter Height (H): "))
            W = int(input("Enter Width (W): "))
            N = int(input("Enter Number of Coins (N): "))
            coins_input = input("Enter Coin Positions (R,C) separated by semicolons: ").strip().split(';')
            coins = [tuple(map(int, coin.split(','))) for coin in coins_input]
            # Validate inputs
            input_validation(H, W, N, coins)
            break  # Exit loop if inputs are valid
        except ValueError as e:
            print(f"Input error: {e}. Please try again.")
    # Calculate maximum coins collected and path
    max_coins_collected, path = max_coins(H, W, N, coins)
    # Display results
    print(f"Max Coins Collected: {max_coins_collected}")
    print("Path: " + " -> ".join(map(str, path)))
if __name__ == "__main__":
    main()