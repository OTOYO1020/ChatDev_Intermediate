'''
Main application file to run the console application for counting level-k stars in a tree.
'''
from tree import Tree
def main():
    input_data = input("Enter the number of edges followed by the edges (u, v) in the format 'u v', each on a new line:\n")
    try:
        tree = Tree(input_data)
        result = tree.count_stars()
        print(result)
    except ValueError as ve:
        print(f"Error: {str(ve)}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()