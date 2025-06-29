'''
Main entry point for the cookie management application.
'''
from cookie_manager import CookieManager
import sys
def main():
    # Read integers H and W from standard input
    H, W = map(int, sys.stdin.readline().strip().split())
    # Initialize a 2D list 'cookies' to store the color of each cookie
    cookies = [list(sys.stdin.readline().strip()) for _ in range(H)]
    # Create a CookieManager instance
    manager = CookieManager(H, W)
    manager.add_cookies(cookies)
    # Perform the marking and removal procedure
    while True:
        manager.mark_cookies()
        if any(any(row) for row in manager.marked):
            manager.remove_marked_cookies()
        else:
            break
    # Count and print the remaining cookies
    remaining_count = manager.count_remaining_cookies()
    print(remaining_count)
if __name__ == "__main__":
    main()