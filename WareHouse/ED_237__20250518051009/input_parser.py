'''
Parses input data for the application.
'''
def parse_input(input_data: str) -> tuple[int, int, list[int], list[tuple[int, int]]]:
    lines = input_data.strip().splitlines()
    N, M = map(int, lines[0].split())
    H = list(map(int, lines[1].split()))
    slopes = [tuple(map(int, line.split())) for line in lines[2:M + 2]]
    return N, M, H, slopes