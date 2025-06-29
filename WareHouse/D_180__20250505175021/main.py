'''
Main application file for the training simulation.
'''
from training import TrainingSimulator
def main():
    '''
    Main function to run the training simulation.
    '''
    try:
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))
        simulator = TrainingSimulator(x, y, a, b)
        exp = simulator.simulate_training()
        print(f"Final EXP: {exp}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()