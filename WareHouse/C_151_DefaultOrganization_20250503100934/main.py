'''
Main application file that handles the submission processing and outputs results.
'''
def validate_submission(p_i, S_i, N):
    errors = []
    if p_i < 1 or p_i > N:
        errors.append(f"Error: Problem index {p_i} is out of range (1 to {N}).")
    if S_i not in ['WA', 'AC']:
        errors.append(f"Error: Verdict '{S_i}' is not valid. Use 'WA' or 'AC'.")
    return errors
def main():
    import sys
    # Read integers N and M
    N, M = map(int, sys.stdin.readline().strip().split())
    penalties = {}
    correct_answers = set()
    error_messages = []
    for _ in range(M):
        p_i, S_i = sys.stdin.readline().strip().split()
        p_i = int(p_i)
        # Validate submission and collect errors
        errors = validate_submission(p_i, S_i, N)
        error_messages.extend(errors)
        if errors:
            continue  # Skip to the next submission if there are errors
        if S_i == 'WA':
            if p_i not in correct_answers:  # Only count WA if AC has not been received
                if p_i not in penalties:
                    penalties[p_i] = 0
                penalties[p_i] += 1
        elif S_i == 'AC':
            correct_answers.add(p_i)
    # Print all collected error messages
    if error_messages:
        for message in error_messages:
            print(message)
    total_correct_answers = len(correct_answers)
    total_penalties = sum(penalties.get(problem, 0) for problem in correct_answers)
    print(total_correct_answers, total_penalties)
if __name__ == "__main__":
    main()