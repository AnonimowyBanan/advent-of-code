from day_interface import DayInterface
from utilis import read_input_data


class Day2(DayInterface):

    def __init__(self, input_data: str):
        self.data = Day2.__parse_data(input_data)

    @staticmethod
    def __parse_data(puzzle_data: str) -> list:
        return [[int(num) for num in row.split('x')] for row in puzzle_data.splitlines()]

    def execute_part1(self):
        wrapping_paper_square = 0
        for box in self.data:
            l, w, h = box
            side1, side2, side3 = l * w, w * h, h * l
            wrapping_paper_square += (2 * side1) + (2 * side2) + (2 * side3) + min(side1, side2, side3)
        return wrapping_paper_square

    def execute_part2(self):
        feet_of_ribbon = 0
        for box in self.data:
            box.sort()
            a, b, c = box
            feet_of_ribbon += (a + a + b + b) + (a * b * c)
        return feet_of_ribbon

day2 = Day2(read_input_data(2015, 2))
print(f'Day 2 part 1: {day2.execute_part1()}')
print(f'Day 2 part 2: {day2.execute_part2()}')