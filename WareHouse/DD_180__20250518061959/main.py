'''
Main entry point for the experience calculator application.
'''
from experience_calculator import max_experience
def main():
    try:
        X = int(input("Enter STR (X): "))
        Y = int(input("Enter Evolution STR (Y): "))
        A = int(input("Enter Kakomon Gym Multiplier (A): "))
        B = int(input("Enter AtCoder Gym Increment (B): "))
        max_exp = max_experience(X, Y, A, B)
        print(f"Maximum Experience: {max_exp}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()