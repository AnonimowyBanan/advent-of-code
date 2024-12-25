def read_input_data(year: int, day: int) -> str:
    try:
        with open(f'../{year}/inputs/day{day}.txt', 'r') as puzzle_input:
            return puzzle_input.read()
    except FileNotFoundError:
        return 'Input file not found'