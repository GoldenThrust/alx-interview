#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


test_cases = [
    (3, [4, 5, 1]),
    
    (5, [2, 5, 1, 4, 3]),
    
    (5, [6, 8, 10, 12, 14]),
    
    (4, [3, 7, 10, 2]),
    
    (3, [9973, 997, 9977]),
    
    (4, [5000, 5001, 5002, 5003]),
    
    (5, [9991, 9992, 9993, 9994, 9995]),
    
    (3, [1, 1, 1]),
    
    (2, [2, 3]),
    
    (3, [4, 5, 1])
]

# Running the test cases
for idx, (rounds, nums) in enumerate(test_cases, 1):
    result = isWinner(rounds, nums)
    print(f"Test case {idx}: Winner: {result}", (rounds, nums))
