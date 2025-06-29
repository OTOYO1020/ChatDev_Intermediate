class Subtask:
    def __init__(self):
        pass
    def solve_problem(self):
        # Read the input sequences A and B
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        # Get the lengths of sequences A and B
        N = len(A)
        M = len(B)
        # Initialize the count of valid indices
        count = 0
        # Iterate over all possible starting indices i
        for i in range(N - M + 1):
            # Get the subsequence C of length M starting from index i
            C = A[i:i+M]
            # Update all elements of B and C that are 0 with any positive real number
            for j in range(M):
                if B[j] == 0:
                    B[j] = 1
                    C[j] = 1
            # Determine the scaling factor t
            t = B[0] / C[0]
            # Check if multiplying all elements of C by t makes B and C identical
            is_identical = True
            for j in range(M):
                if B[j] / C[j] != t:
                    is_identical = False
                    break
            # If B and C are identical, increment the count
            if is_identical:
                count += 1
        # Print the count of valid indices
        print(count)