#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner
# Define the is_prime and isWinner functions as before

# Test examples
examples = [
    ((3, [4, 5, 1]), "Ben"), 
    ((4, [7, 10, 3, 8]), "Ben"), 
    ((2, [15, 20]), "Maria"), 
    ((5, [12, 18, 22, 9, 6]), "Ben"), 
    ((3, [100, 50, 30]), "Ben"), 
    ((4, [17, 21, 33, 24]), "Maria"), 
    ((2, [11, 14]), "Ben"), 
    ((5, [25, 27, 35, 40, 16]), "Maria"), 
    ((3, [45, 60, 75]), "Ben"), 
    ((4, [23, 28, 38, 42]), "Ben"), 
    ((2, [13, 16]), "Maria"), 
    ((5, [55, 66, 77, 88, 99]), "Ben"), 
    ((3, [80, 90, 100]), "Maria"), 
    ((4, [19, 29, 39, 49]), "Ben"), 
    ((2, [18, 23]), "Ben"), 
    ((5, [65, 70, 85, 95, 100]), "Maria"), 
    ((3, [48, 72, 96]), "Ben"), 
    ((4, [31, 47, 61, 83]), "Ben"), 
    ((2, [27, 35]), "Ben"), 
    ((5, [44, 52, 68, 84, 92]), "Ben")
]

# Test the function for each example and check against expected output
for i, (example, expected_output) in enumerate(examples):
    x, nums = example
    result = isWinner(x, nums)
    if result!= expected_output:
        print(f"Test {i + 1} failed. Expected output: {expected_output}, actual output: {result}")