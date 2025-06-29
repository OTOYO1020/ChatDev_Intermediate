from subtask import Subtask
def main():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = [3, 4, 5]
    subtask = Subtask()
    matching_indices = subtask.find_matching_indices(A, B)
    print("Number of matching indices without considering key change:", matching_indices)
    matching_indices_with_key_change = subtask.find_matching_indices_with_key_change(A, B)
    print("Number of matching indices considering key change:", matching_indices_with_key_change)
if __name__ == "__main__":
    main()