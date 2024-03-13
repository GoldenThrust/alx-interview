#!/usr/bin/python3
""" prime game """


def sieve_of_eratosthenes(limit):
    """
    Generate a list of prime numbers up to a specified limit using the Sieve of
    Eratosthenes algorithm.

    Args:
        limit (int): The upper limit (inclusive) within which to find prime
        numbers.

    Returns:
        list: A list of prime numbers within the specified limit.
    """
    primes = []
    sieve = [1] * (limit + 1)

    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)

            for mult in range(num * num, limit + 1, num):
                sieve[mult] = 0
    return primes


def determine_winner(nums):
    """
    Determine the winner between Maria and Ben based on a list of
    numbers.

    Args:
        nums (list): A list of integers representing the rounds of
        the game.

    Returns:
        str: The winner of the game ("Maria" or "Ben").
    """
    try:
        primes = sieve_of_eratosthenes(max(nums))
    except Exception:
        pass

    maria_wins = False
    for n in nums:
        if n in primes:
            maria_wins = not maria_wins

    return "Maria" if maria_wins else "Ben"


def isWinner(x, nums):
    """
    Simulate a game between Maria and Ben and determine the winner
    based on the results.

    Args:
        x (int): The number of rounds to simulate.
        nums (list): A list of integers representing the rounds of the
        game.

    Returns:
        str or None: The winner of the game ("Maria" or "Ben"). Returns
        None if there's a tie.
    """
    if x < 1 or not nums or any(num < 0 for num in nums):
        return None

    counter = 0
    maria = 0
    ben = 0

    for num in nums:
        if counter == x:
            break

        winner = determine_winner(range(1, num + 1))
        if winner == "Maria":
            maria += 1
        elif winner == "Ben":
            ben += 1

        counter += 1

    if maria > ben:
        return "Maria"
    elif maria < ben:
        return "Ben"
    else:
        return None