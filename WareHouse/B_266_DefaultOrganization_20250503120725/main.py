'''
Main entry point for the modulo calculator application.
'''
from modulo_calculator import calculate_modulo
def main():
    try:
        n = int(input("Please enter an integer within the range of -10^18 to 10^18: "))
        result = calculate_modulo(n)
        print(result)
    except ValueError as e:
        print("Invalid input:", e)
if __name__ == "__main__":
    main()