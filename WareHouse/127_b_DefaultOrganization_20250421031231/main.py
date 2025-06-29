'''
Main entry point for the Algae Growth Simulation application.
'''
from algae_growth_simulator import AlgaeGrowthSimulator
def main():
    # Input reception and initialization
    while True:
        try:
            r = int(input("Please enter a non-negative integer for the growth coefficient (r): "))  # Read growth coefficient (r)
            D = int(input("Please enter a non-negative integer for the attrition amount (D): "))  # Read attrition amount (D)
            x_2000 = int(input("Please enter a non-negative integer for the weight of algae in 2000 (x_2000): "))  # Read weight of algae in 2000 (x_2000)
            # Input validation
            if r < 0 or D < 0 or x_2000 < 0:
                print("Error: The values for r, D, and x_2000 must be non-negative integers. Please try again.")
                continue  # Restart the loop for valid inputs
            break  # Exit loop if inputs are valid
        except ValueError:
            print("Error: Please enter valid integers for r, D, and x_2000.")
    # Prepare for growth simulation
    simulator = AlgaeGrowthSimulator(r, D, x_2000)
    results = simulator.simulate_growth()
    # Output processing
    print("Algae weight from 2001 to 2010:")
    for result in results:
        print(result)
if __name__ == "__main__":
    main()