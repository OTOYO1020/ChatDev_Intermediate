'''
Main application file for the Candy Box program.
'''
from candy_box import can_buy_boxes
def main():
    # Parse input values
    N = int(input())
    M = int(input())
    prices = list(map(int, input().split()))
    candies = list(map(int, input().split()))
    possible, total_cost = can_buy_boxes(N, M, prices, candies)
    if possible:
        print(f"possible {total_cost}")
    else:
        print("impossible")
if __name__ == "__main__":
    main()