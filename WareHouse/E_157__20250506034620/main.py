'''
Main application file for the string manipulation application.
'''
from string_manager import StringManager
def main():
    # Read N and Q from standard input
    N, Q = map(int, input().split())
    # Read the string S from standard input
    S = input().strip()
    # Initialize the StringManager with the input string
    string_manager = StringManager(S)
    # Process each query
    for _ in range(Q):
        query = list(input().strip().split())
        query_type = int(query[0])
        if query_type == 1:
            # Update character query
            i_q = int(query[1]) - 1  # Convert to 0-based index
            c_q = query[2]
            string_manager.update_character(i_q, c_q)
        elif query_type == 2:
            # Unique character count query
            l_q = int(query[1]) - 1  # Convert to 0-based index
            r_q = int(query[2])
            unique_count = string_manager.get_unique_count(l_q, r_q)
            print(unique_count)
if __name__ == "__main__":
    main()