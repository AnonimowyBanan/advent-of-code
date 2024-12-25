from day_interface import DayInterface
from utilis import read_input_data
import hashlib


class Day3(DayInterface):

    def __init__(self, input_data: str):
        self.data = input_data

    def __find_start_n_zeros(self, zeros: int):
        new_md5 = hashlib.md5(self.data.encode()).hexdigest()
        postfix_numbers = 0
        while new_md5[:5] != '0' * zeros:
            new_md5 = hashlib.md5(f'{self.data}{postfix_numbers}'.encode()).hexdigest()
            postfix_numbers += 1
        return postfix_numbers - 1

    def execute_part1(self):
        return self.__find_start_n_zeros(5)

    def execute_part2(self):
        return self.__find_start_n_zeros(6)

day3 = Day3(read_input_data(2015, 4))
print(f'Day 4 part 1: {day3.execute_part1()}')
print(f'Day 4 part 2: {day3.execute_part2()}')