'''
Main application file for the children movement simulation.
'''
from simulation import simulate_children
def main():
    '''
    Main function to run the simulation.
    '''
    movement_string = input("Enter movement string (L/R): ")
    if all(c in 'LR' for c in movement_string) and 2 <= len(movement_string) <= 100000:
        results = simulate_children(movement_string)
        print("Children on each square:", results)
    else:
        print("Input Error: Please enter a valid string of 'L' and 'R'.")
if __name__ == "__main__":
    main()