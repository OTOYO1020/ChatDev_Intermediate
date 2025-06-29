'''
Main application file for the product purchase calculator.
'''
from utils import validate_input  # Import the validate_input function
def calculate_total_cost(prices):
    '''
    Calculate the total cost of products based on their prices.
    Discounts are applied to products at even indices.
    '''
    total_cost = 0
    for i in range(len(prices)):
        if i % 2 == 0:  # even index
            discounted_price = max(prices[i] - 1, 0)  # Ensure no negative price
            total_cost += discounted_price
        else:  # odd index
            total_cost += prices[i]
    return total_cost
def main():
    # Read input values
    while True:
        n = input("Enter the number of products (N): ")
        if validate_input(n):
            n = int(n)
            break
        print("Error: N must be a positive integer greater than zero.")
    # Process prices
    prices = []
    for i in range(n):
        while True:
            price = input(f"Enter price for product {i + 1}: ")
            if validate_input(price):
                prices.append(int(price))
                break
            print("Error: Please enter a valid positive integer for the price.")
    while True:
        budget = input("Enter your budget (X): ")
        if validate_input(budget):
            budget = int(budget)
            break
        print("Error: Budget must be a positive integer greater than zero.")
    total_cost = calculate_total_cost(prices)
    if total_cost <= budget:
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()