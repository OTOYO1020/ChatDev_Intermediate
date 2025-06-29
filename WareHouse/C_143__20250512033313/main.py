'''
Main application file for the Slime Counter application.
'''
from slime_counter import count_fused_slimes
def main():
    slime_colors = input("Enter Slime Colors: ")
    result = count_fused_slimes(slime_colors)
    print(f"Distinct Slimes: {result}")
if __name__ == "__main__":
    main()