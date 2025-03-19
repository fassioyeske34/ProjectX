import random

def get_random_number(low=1, high=6):
    """
    Generates a random number between low and high (inclusive).
    :param low: The lower bound of the range. Default is 1.
    :param high: The upper bound of the range. Default is 6.
    :return: A random integer between low and high.
    """
    return random.randint(low, high)
