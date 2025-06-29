'''
Contains the game logic for managing Takahashi's movements and health.
'''
class TakahashiGame:
    def __init__(self):
        self.health = 0  # Initial health
        self.position = (0, 0)  # Starting position
        self.health_items = set()  # Health items set
        self.max_health = 0  # Maximum health
        self.health_threshold = 0  # Health threshold for recovery
    def start_game(self):
        # Read N, M, H, K from input
        N, M, H, K = map(int, input().split())
        self.health = H  # Set initial health
        self.max_health = H  # Set maximum health
        self.health_threshold = K  # Set health threshold for recovery
        # Read health item coordinates
        for _ in range(M):
            x, y = map(int, input().split())
            self.health_items.add((x, y))
        # Read the move string S
        moves = input().strip()
        self.process_moves(moves)
    def process_moves(self, moves):
        for move in moves:
            self.move_takahashi(move)
            if self.health < 0:
                print("NO")
                return
            self.check_health_item()  # Check for health item after each move
        print("YES")
    def move_takahashi(self, direction):
        x, y = self.position
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        # Check for out of bounds (assuming Takahashi cannot go below (0, 0))
        if x < 0 or y < 0:
            print("NO")
            exit()  # Terminate the program immediately
        # Update position
        self.position = (x, y)
        self.health -= 1  # Decrease health for each move
    def check_health_item(self):
        if self.position in self.health_items:
            if self.health < self.health_threshold:
                self.health = min(self.health_threshold, self.max_health)  # Recover health to K but not exceed max health