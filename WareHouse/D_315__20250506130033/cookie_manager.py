'''
This module manages the cookies and their removal based on specified rules.
'''
class CookieManager:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cookies = [['' for _ in range(width)] for _ in range(height)]
        self.marked = [[False for _ in range(width)] for _ in range(height)]
    def add_cookies(self, cookie_colors):
        for i in range(self.height):
            self.cookies[i] = list(cookie_colors[i])
    def mark_cookies(self):
        # Reset marked based on current dimensions of cookies
        self.marked = [[False for _ in range(len(self.cookies[0]))] for _ in range(len(self.cookies))]
        # Mark rows
        for i in range(len(self.cookies)):
            color_count = {}
            for color in self.cookies[i]:
                if color in color_count:
                    color_count[color] += 1
                else:
                    color_count[color] = 1
            for color, count in color_count.items():
                if count >= 2:
                    for j in range(len(self.cookies[i])):
                        if self.cookies[i][j] == color:
                            self.marked[i][j] = True
        # Mark columns
        for j in range(len(self.cookies[0])):
            color_count = {}
            for i in range(len(self.cookies)):
                color = self.cookies[i][j]
                if color in color_count:
                    color_count[color] += 1
                else:
                    color_count[color] = 1
            for color, count in color_count.items():
                if count >= 2:
                    for i in range(len(self.cookies)):
                        if self.cookies[i][j] == color:
                            self.marked[i][j] = True
    def remove_marked_cookies(self):
        new_cookies = []
        for i in range(self.height):
            new_row = []
            for j in range(self.width):
                if not self.marked[i][j]:
                    new_row.append(self.cookies[i][j])
            if new_row:  # Only add non-empty rows
                new_cookies.append(new_row)
        # Update the cookies and dimensions
        self.cookies = new_cookies
        self.height = len(new_cookies)  # Update height
        self.width = max(len(row) for row in new_cookies) if new_cookies else 0  # Update width based on the longest row
        # Reset marked to match the current dimensions of cookies
        self.marked = [[False for _ in range(self.width)] for _ in range(self.height)]
    def count_remaining_cookies(self):
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if not self.marked[i][j]:  # Count only unmarked cookies
                    count += 1
        return count