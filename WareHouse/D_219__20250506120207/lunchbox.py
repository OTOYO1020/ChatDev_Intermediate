'''
Module containing Lunchbox and LunchboxManager classes.
'''
class Lunchbox:
    def __init__(self, takoyaki, taiyaki):
        self.takoyaki = takoyaki
        self.taiyaki = taiyaki
class LunchboxManager:
    def __init__(self):
        self.lunchboxes = []
    def add_lunchbox(self, lunchbox):
        self.lunchboxes.append(lunchbox)
    def find_min_lunchboxes(self, x, y):
        '''
        This method uses dynamic programming to find the minimum number of lunchboxes
        needed to achieve at least x takoyaki and y taiyaki. It initializes a DP table
        where dp[i][j] represents the minimum number of lunchboxes needed to achieve
        at least i takoyaki and j taiyaki.
        '''
        # Check if both x and y are zero
        if x == 0 and y == 0:
            return 0  # No lunchboxes needed
        # Initialize a DP table
        dp = [[float('inf')] * (y + 1) for _ in range(x + 1)]
        dp[0][0] = 0  # 0 lunchboxes needed to achieve 0 takoyaki and 0 taiyaki
        # Iterate through each lunchbox
        for lunchbox in self.lunchboxes:
            # Update the DP table in reverse order to avoid overwriting results
            for takoyaki in range(x, -1, -1):
                for taiyaki in range(y, -1, -1):
                    new_takoyaki = min(takoyaki + lunchbox.takoyaki, x)
                    new_taiyaki = min(taiyaki + lunchbox.taiyaki, y)
                    dp[new_takoyaki][new_taiyaki] = min(dp[new_takoyaki][new_taiyaki], dp[takoyaki][taiyaki] + 1)
        return dp[x][y] if dp[x][y] != float('inf') else -1