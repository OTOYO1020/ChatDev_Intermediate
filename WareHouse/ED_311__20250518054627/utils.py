'''
Utility module for helper functions, including parsing input data.
'''
def parse_input(input_string: str, N: int, H: int, W: int) -> list:
    if N == 0:
        return []
    if N > H * W:
        raise ValueError(f"Cannot have more holed squares ({N}) than total squares ({H * W}).")
    holed_squares = []
    pairs = input_string.split()
    for pair in pairs:
        try:
            x, y = map(int, pair.strip("()").split(","))
            if 0 <= x < H and 0 <= y < W:  # Check if coordinates are within bounds
                holed_squares.append((x, y))
            else:
                raise ValueError(f"Holed square coordinates ({x}, {y}) are out of bounds.")
        except ValueError:
            raise ValueError(f"Invalid format for holed square: {pair}. Expected format is (x,y).")
    if len(holed_squares) != N:
        raise ValueError(f"Expected {N} holed squares, but got {len(holed_squares)}.")
    return holed_squares