'''
Utility functions for the project manager application.
'''
def validate_input(N, K, employees):
    '''
    Validates the input values for departments and employees.
    '''
    if K > N:
        return False
    if len(employees) != N:
        return False
    return True
def calculate_max_projects(N, K, employees):
    '''
    Calculates the maximum number of projects that can be formed.
    '''
    if K > N:
        return 0
    # Sort employees in descending order
    employees.sort(reverse=True)
    max_projects = 0
    # Continue forming projects while all K departments have at least one employee
    while True:
        # Check if we can form a project with the first K departments
        if all(emp > 0 for emp in employees[:K]):
            for i in range(K):
                employees[i] -= 1  # Decrement the employee count for the first K departments
            max_projects += 1  # Increment the project count
        else:
            break  # Exit the loop if any of the first K departments has no employees left
        # Re-sort the employees after decrementing to maintain the order
        employees.sort(reverse=True)
    return max_projects