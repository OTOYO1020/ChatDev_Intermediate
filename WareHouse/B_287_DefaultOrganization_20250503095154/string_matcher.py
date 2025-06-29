'''
This module contains the StringMatcherApp class which implements the logic
for string matching based on user input without a GUI.
'''
class StringMatcherApp:
    def run(self):
        n = int(input("Enter number of strings (N): "))
        m = int(input("Enter number of matches (M): "))
        S = []
        for i in range(n):
            S_i = self.get_valid_input(f"Enter string {i + 1} (must be exactly 6 characters long): ", 6)
            S.append(S_i)
        print(f"Collected {len(S)} valid strings for S.")
        T = []
        for j in range(m):
            T_j = self.get_valid_input(f"Enter match {j + 1} (must be exactly 3 characters long): ", 3)
            T.append(T_j)
        print(f"Collected {len(T)} valid matches for T.")
        if not S or not T:
            print("No valid strings or matches were collected. Exiting.")
            return
        count = self.get_match_count(S, T)
        print(count)
    def get_valid_input(self, prompt, expected_length):
        """Prompts the user for input until a valid string of the expected length is provided."""
        while True:
            user_input = input(prompt)
            if len(user_input) == expected_length:
                return user_input
            else:
                print(f"Error: Input must be exactly {expected_length} characters long. Please try again.")
    def get_match_count(self, strings, matches):
        """Counts how many strings in 'strings' have their last three characters in 'matches'."""
        count = 0
        match_set = set(matches)
        for s in strings:
            if s[-3:] in match_set:
                count += 1
        return count