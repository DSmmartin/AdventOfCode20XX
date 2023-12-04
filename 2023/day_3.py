# PART 1

"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much large

"""

import re

# input_engine_schematic = [
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598..",
# ]

FILE_INPUT = '/workspaces/AdventOfCode20XX/2023/day_3_input'

def read_input_file(name):
    with open(name) as input_file:
        list_input = input_file.read().splitlines()
    return list_input

input_engine_schematic = read_input_file(FILE_INPUT)

MAX_INDEX_CODES = len(input_engine_schematic) - 1
MAX_CHAR_INDEX_LIMIT = len(input_engine_schematic[0]) - 1

def cut_limit_min(value):
    return (value < 0) * 0 + (value >= 0) * value

def cut_limit_max(value, limit_max):
    return (value > limit_max) * limit_max + (value <= limit_max) * value

def clean_strings(codes):
    return re.sub(r"\d|(\.)", "", codes)

valid_codes = 0

for code in range(len(input_engine_schematic)):
    codes_raw = input_engine_schematic[code]
    pair_number_founds = [(number_index.start(), number_index.end()) for number_index in re.finditer(r"(\d{1,3})", codes_raw)]

    upper_code = cut_limit_min(code - 1)
    middle_code = code
    bottom_code = cut_limit_max(code + 1, MAX_INDEX_CODES)
    for start_index_to_eval, end_index_to_eval in pair_number_founds:
        candidate_number = input_engine_schematic[middle_code][start_index_to_eval:end_index_to_eval]
        start_index = cut_limit_min(start_index_to_eval - 1)
        end_index = cut_limit_max(end_index_to_eval + 1, MAX_CHAR_INDEX_LIMIT)

        string_upper_to_clean = input_engine_schematic[upper_code][start_index:end_index]
        string_middle_to_clean = input_engine_schematic[middle_code][start_index:end_index]
        string_botton_to_clean = input_engine_schematic[bottom_code][start_index:end_index]

        strings_with_symbol = clean_strings(string_upper_to_clean + string_middle_to_clean + string_botton_to_clean)

        valid_codes += (len(strings_with_symbol) > 0) * int(candidate_number)

print('sum codes {}'.format(valid_codes)) 