'''
Main application file for ID Card Gate application.
'''
from utils import validate_input, validate_gate_range
def main():
    '''
    Main function to run the ID Card Gate application.
    '''
    try:
        # Receiving input and initialization
        n = input("Enter the number of ID Cards (N): ")
        while not validate_input(n):
            n = input("Invalid input. Please enter a positive integer for ID Cards (N): ")
        n = int(n)
        m = input("Enter the number of Gates (M): ")
        while not validate_input(m):
            m = input("Invalid input. Please enter a positive integer for Gates (M): ")
        m = int(m)
        gates = []
        for _ in range(m):
            while True:  # Keep asking until valid input
                gate_input = input("Enter gate range (L, R): ")
                if validate_gate_range(gate_input):
                    l, r = map(int, gate_input.split(','))
                    gates.append((l, r))
                    break
                else:
                    print("Invalid input. Please enter the gate range in the format 'L,R' where L is less than or equal to R.")
        # Check if there are no gates
        if not gates:  # Check if gates list is empty
            print("No gates were entered. Please provide at least one gate range.")  # Inform the user
            return  # Exit the main function early
        # Calculating the intersection of the passable range
        L_max = max(l for l, r in gates)
        R_min = min(r for l, r in gates)
        # Check if there is an intersection
        count = max(0, R_min - L_max + 1)  # Count of ID cards in the intersection range, ensuring non-negative count
        # Outputting the result
        print(count)
    except ValueError:
        print("Input Error: Please enter valid numbers for ID cards and gates.")
if __name__ == "__main__":
    main()