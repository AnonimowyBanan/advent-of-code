from day_interface import DayInterface
from utilis import read_input_data

class Day1(DayInterface):

    def __init__(self, input_data: str):
        self.data = input_data

    def execute_part1(self):
        return self.data.count('(') - self.data.count(')')

    def execute_part2(self):
        up_count = down_count = 0
        for i, char in enumerate(self.data):
            if char == '(':
                up_count += 1
            elif char == ')':
                down_count += 1

            if down_count > up_count:
                return i + 1

day1 = Day1(read_input_data(2015, 1))
print(f'Day 1 part 1: {day1.execute_part1()}')
print(f'Day 1 part 2: {day1.execute_part2()}')