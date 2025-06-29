'''
Main application file for the player comfort calculation.
'''
def main():
    try:
        n = int(input("Enter the number of players: "))
        friendliness_values = list(map(int, input("Enter friendliness values separated by spaces: ").split()))
        if len(friendliness_values) != n:
            raise ValueError("Number of friendliness values must match N.")
        from comfort_calculator import ComfortCalculator
        calculator = ComfortCalculator(friendliness_values)
        total_comfort = calculator.calculate_total_comfort()
        print(total_comfort)
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()