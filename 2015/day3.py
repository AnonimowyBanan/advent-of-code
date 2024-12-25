from day_interface import DayInterface
from utilis import read_input_data
from collections import OrderedDict


class Day3(DayInterface):

    def __init__(self, input_data: str):
        self.data = input_data

    @staticmethod
    def __give_away_gifts(route: list|str):
        locations_of_visited_houses = []
        for direction in route:
            x, y = locations_of_visited_houses[-1] if len(locations_of_visited_houses) > 0 else [0, 0]
            if direction == '^':
                y -= 1
            if direction == '>':
                x += 1
            if direction == 'v':
                y += 1
            if direction == '<':
                x -= 1
            locations_of_visited_houses.append([x, y])
        return locations_of_visited_houses

    @staticmethod
    def __remove_duplicates(house_localizations: list|str):
        return OrderedDict((tuple(x), x) for x in house_localizations).values()

    def execute_part1(self):
        return len(Day3.__remove_duplicates(Day3.__give_away_gifts(self.data)))

    def execute_part2(self):
        houses_locations = []
        santa_routes = [self.data[::2], self.data[1::2]]
        for route in santa_routes:
            houses_locations.append(Day3.__give_away_gifts(route))
        flatten_houses_locations_array = [element for sublist in houses_locations for element in sublist]
        return len(Day3.__remove_duplicates(flatten_houses_locations_array))

day3 = Day3(read_input_data(2015, 3))
print(f'Day 3 part 1: {day3.execute_part1()}')
print(f'Day 3 part 2: {day3.execute_part2()}')