'''
Main application file for the movie and gameplay duration calculator.
'''
def calculate_total_time(N, X, A, B):
    total_time = 0
    for i in range(1, N + 1):
        # Add movie time and gameplay time for the first clear of stage i
        total_time += A[i - 1] + B[i - 1]  
        # Add gameplay time for subsequent clears of stage i (X - 1 times)
        if X > 1:  # Only add if there are subsequent clears
            total_time += (X - 1) * B[i - 1]   
    return total_time
if __name__ == "__main__":
    try:
        N = int(input("Enter number of stages (N): "))
        X = int(input("Enter number of clears (X): "))
        if N <= 0 or X <= 0:
            raise ValueError("N and X must be positive integers.")
        A = list(map(int, input("Enter movie durations (comma-separated): ").split(',')))
        B = list(map(int, input("Enter gameplay durations (comma-separated): ").split(',')))
        if len(A) != N or len(B) != N:
            raise ValueError("The lengths of movie durations and gameplay durations must match N.")
        # New validation for non-negative durations
        if any(a < 0 for a in A) or any(b < 0 for b in B):
            raise ValueError("Movie and gameplay durations must be non-negative integers.")
        total_time = calculate_total_time(N, X, A, B)
        print(f"Total Time: {total_time}")
    except ValueError as e:
        print(f"Input error: {e}")