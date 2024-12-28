from day_interface import DayInterface
from utilis import read_input_data


def parse_data(data: list):
    parsed_data = []
    for line in data:
        splitted = line.split(' through ')
        coordinates = splitted[0]
        action = 'toggle'
        if 'turn on' in coordinates:
            action = 'turn_on'
        elif 'turn off' in coordinates:
            action = 'turn_off'
        coordinates = coordinates.replace('toggle ', '').replace('turn on ', '').replace('turn off ', '')
        parsed_data.append({
            'action': action,
            'start': [int(number) for number in coordinates.split(',')],
            'through': [int(number) for number in splitted[1].split(',')]
        })
    return parsed_data

def create_matrix():
    return [[0 for _ in range(10000)] for _ in range(1000)]

def count_lights(matrix) -> int:
    return sum(sum(row) for row in matrix)


class Day6(DayInterface):

    def __init__(self, input_data: str):
        self.data = parse_data(input_data.splitlines())

    def execute_part1(self):
        matrix = create_matrix()
        for instruction in self.data:
            for row_index in range(instruction.get('start')[0], instruction.get('through')[0] + 1):
                for column_index in range(instruction.get('start')[1], instruction.get('through')[1] + 1):
                    if instruction.get('action') == 'toggle':
                        matrix[row_index][column_index] = 1 if matrix[row_index][column_index] == 0 else 0
                    elif instruction.get('action') == 'turn_on':
                        matrix[row_index][column_index] = 1
                    elif instruction.get('action') == 'turn_off':
                        matrix[row_index][column_index] = 0
        return count_lights(matrix)

    def execute_part2(self):
        matrix = create_matrix()
        for instruction in self.data:
            for row_index in range(instruction.get('start')[0], instruction.get('through')[0] + 1):
                for column_index in range(instruction.get('start')[1], instruction.get('through')[1] + 1):
                    if instruction.get('action') == 'toggle':
                        matrix[row_index][column_index] += 2
                    elif instruction.get('action') == 'turn_on':
                        matrix[row_index][column_index] += 1
                    elif instruction.get('action') == 'turn_off':
                        matrix[row_index][column_index] -= 1 if matrix[row_index][column_index] != 0 else 0
        return count_lights(matrix)

day6 = Day6(read_input_data(2015, 6))
print(f'Day 6 part 1: {day6.execute_part1()}')
print(f'Day 6 part 2: {day6.execute_part2()}')