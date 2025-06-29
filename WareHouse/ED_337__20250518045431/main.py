'''
Main application file for identifying spoiled juice bottles using standard input and output.
'''
from bottle_distribution import BottleDistribution
import sys
import math
def main():
    try:
        total_bottles = int(input().strip())  # Read the number of juice bottles
        if total_bottles <= 0:
            print("Error: The number of bottles must be a positive integer.")
            return
        # Calculate the minimum number of friends needed
        num_friends = math.ceil(math.log2(total_bottles)) if total_bottles > 1 else 1
        # Ensure num_friends does not exceed total_bottles
        if num_friends > total_bottles:
            num_friends = total_bottles
        distribution = BottleDistribution(total_bottles)
        friends_bottles = distribution.distribute_bottles(num_friends)
        print(num_friends)
        for friend_id in range(1, num_friends + 1):
            print(f"{len(friends_bottles[friend_id])} {' '.join(map(str, friends_bottles[friend_id]))}")
            sys.stdout.flush()  # Flush output to avoid TLE
        # Simulate receiving results from the judge
        response_string = input().strip()  # Read the response string
        if len(response_string) != num_friends:
            print(f"Warning: Expected response string length {num_friends}, but got {len(response_string)}.")
            return
        # Initialize a list to track sets of bottles for each upset friend
        upset_bottles = []
        for i in range(num_friends):
            if response_string[i] == '1':
                # Add the set of bottles served to this friend to the list
                upset_bottles.append(set(friends_bottles[i + 1]))  # i + 1 for 1-indexing
        # Identify possible spoiled bottles
        if upset_bottles:
            possible_spoiled_bottles = set.union(*upset_bottles)
            if len(possible_spoiled_bottles) == 1:
                identified_spoiled_bottle = possible_spoiled_bottles.pop()
                print(identified_spoiled_bottle)  # Print the single identified bottle
            else:
                print("Error: Unable to uniquely identify the spoiled bottle.")
        else:
            print("No friends reported an upset stomach.")
        sys.stdout.flush()  # Flush the output
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()