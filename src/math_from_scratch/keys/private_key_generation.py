import random


def generate_private_key(length) -> int:
    # Basically, simulates the coin flip 256 times.
    return random.getrandbits(length)
