import random

def generate_random_python_code():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    # Generate a random string of length 5
    str = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(5))

    # Generate a random list of numbers
    lst = [random.randint(1, 10) for i in range(5)]

    return f"{num} {str} {lst}"
