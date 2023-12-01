# PART 1

"""
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

"""
import string

def read_input_file(name):
    with open(name) as input_file:
        list_input = input_file.readlines()
    return list_input

def clean_input_file(list_input):
    return [item.strip('\n') for item in list_input]

def obtain_input_list_cleaned(file_path):
    list_input = read_input_file(file_path)
    return clean_input_file(list_input)


def obtain_two_digits(list_input):
    list_delete_letters = [item.strip(string.ascii_letters) for item in list_input]
    return [int(item[0] + item[-1]) for item in list_delete_letters]



list_cleaned = obtain_input_list_cleaned('/workspaces/AdventOfCode20XX/2023/day_1_input1')
pair_numbers = obtain_two_digits(list_cleaned)
result = sum(pair_numbers)


# PART 2
"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters:
    one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

"""

input_raw = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"

REPLACE_NUMBERS = [
    ("1", "one"),
    ("2", "two"),
    ("3", "three"),
    ("4", "four"),
    ("5", "five"),
    ("6", "six"),
    ("7", "seven"),
    ("8", "eight"),
    ("9", "nine")
    ]


for number_int, number_str in REPLACE_NUMBERS:
    input_raw = input_raw.replace(number_str, number_int)

#### PROBLEM WITH NUMBER 24


list_translated = input_raw.split('\n')
input_processed = clean_input_file(list_translated)


pair_numbers = obtain_two_digits(input_processed)
result = sum(pair_numbers)