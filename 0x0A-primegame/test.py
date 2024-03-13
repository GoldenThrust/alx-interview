#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner
# Define the is_prime and isWinner functions as before


examples = [
    ((5, [2, 5, 1, 4, 3]), "Ben"),
    ((3, [4, 5, 1]), "Ben"),
    ((0, [4, 3]), None),
    ((5, [1, 2, 3, 4, 5]), "Ben"),
    ((10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2]), "Maria"),
    ((4, [11, 30, 1, 7]), "Ben"),
    ((6, [1, 1, 0, 0, 1, 8]), "Ben"),
    ((1, [1]), "Ben"),
    ((0, [0]), None),
    ((-1, [10]), None)
]


for i, (example, expected_output) in enumerate(examples):
    x, nums = example
    result = isWinner(x, nums)
    print(f"Test {i + 1}. Expected output: {expected_output}, actual output: {result}")
