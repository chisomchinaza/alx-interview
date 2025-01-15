#!/usr/bin/python3
"""
Prime Game Solution
"""


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(max_n):
    """
    Generate a list of prime numbers up to max_n
    using the Sieve of Eratosthenes.
    """
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    return [i for i in range(max_n + 1) if primes[i]]


def isWinner(x, nums):
    """
    Determine the winner of the prime game.
    :param x: Number of rounds
    :param nums: Array of integers representing the upper bound for each round
    :return: Name of the player with the most wins or None
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes_up_to_n = [p for p in primes if p <= n]
        move_count = len(primes_up_to_n)

        if move_count % 2 == 1:
            wins["Maria"] += 1  # Maria wins if odd moves
        else:
            wins["Ben"] += 1  # Ben wins if even moves

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None
