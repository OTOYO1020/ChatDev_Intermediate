'''
The main entry point for the Lunlun Number Finder application.
'''
from lunlun import find_kth_lunlun_number
def main():
    """
    The main function to read input and find the K-th lunlun number.
    """
    try:
        K = int(input("Enter K (1 ≤ K ≤ 100000): "))
        if 1 <= K <= 100000:
            result = find_kth_lunlun_number(K)
            print(f"The {K}-th lunlun number is: {result}")
        else:
            print("K must be between 1 and 100000.")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()