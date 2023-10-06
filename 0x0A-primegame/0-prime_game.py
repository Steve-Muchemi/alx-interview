#!/usr/bin/python3


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        available_numbers = set(range(1, n + 1))

        maria_turn = True
        while True:
            valid_moves = [p for p in primes if p in available_numbers]
            if not valid_moves:
                # No prime numbers left to choose from, the other player wins.
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            # Make a move.
            move = max(valid_moves) if maria_turn else min(valid_moves)
            available_numbers -= set(range(move, n + 1, move))

            # Switch to the other player's turn.
            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
