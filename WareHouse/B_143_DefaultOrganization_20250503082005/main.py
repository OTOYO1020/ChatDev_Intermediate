'''
Main application file for the Takoyaki Health Points Calculator.
'''
def main():
    while True:
        try:
            # Read the number of Takoyaki from user input
            n = int(input("Enter the number of Takoyaki (positive integer): "))
            if n <= 0:
                print("Number of Takoyaki must be a positive integer. Please try again.")
                continue
            # Prompt for deliciousness values
            deliciousness_input = input(f"Please enter exactly {n} deliciousness values, separated by spaces: ")
            deliciousness = list(map(int, deliciousness_input.split()))
            # Validate that the number of deliciousness values matches N
            if len(deliciousness) != n:
                print(f"Number of deliciousness values must match N ({n}). Please try again.")
                continue
            total_health_points = 0
            # Calculate total health points from unique pairs
            for i in range(n):
                for j in range(i + 1, n):
                    total_health_points += deliciousness[i] * deliciousness[j]
            # Output the total health points
            print(total_health_points)
            break  # Exit the loop after successful execution
        except ValueError:
            print("All deliciousness values must be integers. Please check your input and try again.")
if __name__ == "__main__":
    main()