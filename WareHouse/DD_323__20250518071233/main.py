'''
Main application file for the Slime Synthesizer.
'''
from slime_synthesizer import SlimeSynthesizer
def main():
    '''
    Main function to handle input and output for the Slime Synthesizer.
    '''
    try:
        # Read input values
        N = int(input("Enter the number of sizes: "))
        sizes = list(map(int, input("Enter sizes (comma-separated): ").split(',')))
        counts = list(map(int, input("Enter counts (comma-separated): ").split(',')))
        if len(sizes) != len(counts):
            raise ValueError("Sizes and counts must have the same length.")
        synthesizer = SlimeSynthesizer()
        result = synthesizer.min_slimes(N, sizes, counts)
        print(f"Minimum slimes remaining: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()