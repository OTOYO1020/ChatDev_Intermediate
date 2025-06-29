'''
Main application file for the ball placement application.
'''
class MainApp:
    def calculate_balls(self, N, a):
        balls = [0] * N
        # First pass to determine where to place balls
        for i in range(1, N + 1):
            count = 0  # Reset count for each i
            # Check multiples of i
            for j in range(i, N + 1, i):
                count += balls[j - 1]
            # Check if the current count matches the required parity
            if count % 2 != a[i - 1]:
                balls[i - 1] = 1  # Place a ball in the i-th box
                # Update counts for all multiples of i
                for j in range(i, N + 1, i):
                    balls[j - 1] += 1  # Increment the ball count for the j-th box
        # Final verification of the configuration
        for i in range(1, N + 1):
            count = 0  # Reset count for verification
            for j in range(i, N + 1, i):
                count += balls[j - 1]
            if count % 2 != a[i - 1]:
                return "NO"
        return " ".join(map(str, balls))
def main():
    N = int(input())
    a = list(map(int, input().split()))
    if len(a) != N or any(x not in (0, 1) for x in a):
        print("Invalid input.")
        return
    app = MainApp()
    result = app.calculate_balls(N, a)
    print(result)
if __name__ == "__main__":
    main()