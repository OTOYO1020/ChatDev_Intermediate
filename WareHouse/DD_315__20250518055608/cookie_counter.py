'''
Contains the function to count remaining cookies after marking duplicates.
'''
from typing import List
def count_remaining_cookies(H: int, W: int, cookies: List[List[str]]) -> int:
    # Check for uniform row lengths
    if any(len(row) != W for row in cookies):
        raise ValueError("All rows must have the same number of columns.")
    while True:
        marked = set()
        # Check rows for duplicates
        for row in range(H):
            color_count = {}
            for col in range(W):
                color = cookies[row][col]
                if color in color_count:
                    color_count[color] += 1
                else:
                    color_count[color] = 1
            for color, count in color_count.items():
                if count >= 2:
                    for col in range(W):
                        if cookies[row][col] == color:
                            marked.add((row, col))
        # Check columns for duplicates
        for col in range(W):
            color_count = {}
            for row in range(H):
                color = cookies[row][col]
                if color in color_count:
                    color_count[color] += 1
                else:
                    color_count[color] = 1
            for color, count in color_count.items():
                if count >= 2:
                    for row in range(H):
                        if cookies[row][col] == color:
                            marked.add((row, col))
        # If no cookies are marked, break the loop
        if not marked:
            break
        # Remove marked cookies
        new_cookies = []
        for row in range(H):
            new_row = []
            for col in range(W):
                if (row, col) not in marked:
                    new_row.append(cookies[row][col])
            if new_row:  # Only add non-empty rows
                new_cookies.append(new_row)
        # Update cookies to the new list
        cookies = new_cookies
        # Update dimensions immediately after removing marked cookies
        H = len(cookies)
        if H == 0:  # If there are no rows left, break the loop
            break
        # Update W based on the new cookies structure
        W = max(len(row) for row in cookies) if cookies else 0  # Ensure W is updated correctly
    # Count remaining cookies
    remaining_count = sum(len(row) for row in cookies)
    return remaining_count