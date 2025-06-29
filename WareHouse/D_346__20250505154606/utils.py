'''
Utility functions for input validation and cost calculation.
'''
def validate_input(n, s, c):
    '''
    Validates the user input for length, string, and costs.
    '''
    try:
        if n <= 0 or len(s) != n:
            return False
        if len(c) != n:
            return False
        return True
    except ValueError:
        return False
def calculate_cost(n, s, c):
    '''
    Calculates the minimum cost to convert the string S into a good string.
    '''
    min_cost = float('inf')
    for i in range(n - 1):
        # If S[i] is already equal to S[i+1], continue to the next iteration
        if s[i] == s[i + 1]:
            continue
        # Scenario 1: Make S[i] the same as S[i+1]
        total_cost1 = c[i]  # Cost to change S[i] to S[i+1]
        # Scenario 2: Make S[i+1] the same as S[i]
        total_cost2 = c[i + 1]  # Cost to change S[i+1] to S[i]
        # Scenario 3: Change both to '0'
        total_cost3 = (c[i] + c[i + 1]) if (s[i] != '0' and s[i + 1] != '0') else 0
        # Scenario 4: Change both to '1'
        total_cost4 = (c[i] + c[i + 1]) if (s[i] != '1' and s[i + 1] != '1') else 0
        # Update min_cost with the minimum of the current min_cost and the costs from all scenarios
        min_cost = min(min_cost, total_cost1, total_cost2, total_cost3, total_cost4)
    return min_cost if min_cost != float('inf') else -1