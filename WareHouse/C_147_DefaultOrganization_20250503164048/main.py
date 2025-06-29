'''
Main application file for the Honesty Testimony application.
'''
from honesty_calculator import is_honest
def main():
    N = int(input("Enter number of people: "))
    testimonies = []
    for i in range(N):
        A_i = int(input(f"Enter number of testimonies for person {i + 1}: "))
        person_testimonies = []
        for j in range(A_i):
            x_ij, y_ij = map(int, input(f"Enter testimony {j + 1} for person {i + 1} (x y): ").split())
            person_testimonies.append((x_ij, y_ij))
        testimonies.append(person_testimonies)
    max_honest_count = get_max_honest_count(N, testimonies)
    print(f"Max Honest Persons: {max_honest_count}")
def get_max_honest_count(N, testimonies):
    '''
    Calculate the maximum number of honest persons based on testimonies.
    Parameters:
    N (int): The number of people.
    testimonies (list): A list of testimonies for each person.
    Returns:
    int: The maximum count of honest persons found.
    '''
    max_honest_count = 0
    for i in range(1 << N):
        possible_honest = {j for j in range(N) if (i & (1 << j))}
        if is_honest(possible_honest, testimonies):  # Check if the testimonies are consistent
            max_honest_count = max(max_honest_count, len(possible_honest))
    return max_honest_count
if __name__ == "__main__":
    main()