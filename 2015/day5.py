import string

from day_interface import DayInterface
from utilis import read_input_data


class Day3(DayInterface):

    def __init__(self, input_data: str):
        self.data = input_data.splitlines()
        self.allowed_vowels = ['a', 'e', 'i', 'o', 'u']
        self.forbidden_strings = ['ab', 'cd', 'pq', 'xy']
        self.pairs_of_letters = [''.join([letter, new_letter]) for letter in string.ascii_lowercase for new_letter in string.ascii_lowercase]

    def execute_part1(self):
        nice_strings = 0
        for row in self.data:
            vowels_count = sum(row.count(vowel) for vowel in self.allowed_vowels if vowel in row)
            double_letters = sum(row.count(letter) for letter in string.ascii_lowercase if letter * 2 in row)
            forbidden_strings = sum(1 for forbidden_string in self.forbidden_strings if forbidden_string in row)
            if forbidden_strings == 0 and vowels_count >= 3 and double_letters >= 1:
                nice_strings += 1
        return nice_strings

    @staticmethod
    def has_repeating_letter_with_gap(s: str) -> bool:
        for i in range(len(s) - 2):
            if s[i] == s[i + 2]:
                return True
        return False

    def check_if_string_contains_pair_of_any_two_letters(self, s: str) -> bool:
        for pair in self.pairs_of_letters:
            if s.count(pair) >= 2:
                return True
        return False

    def execute_part2(self):
        nice_strings = 0
        for row in self.data:
            if self.check_if_string_contains_pair_of_any_two_letters(row) and self.has_repeating_letter_with_gap(row):
                nice_strings += 1
        return nice_strings

day3 = Day3(read_input_data(2015, 5))
print(f'Day 5 part 1: {day3.execute_part1()}')
print(f'Day 5 part 2: {day3.execute_part2()}')