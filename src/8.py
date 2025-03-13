import random

def get_random_string():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    length = random.randint(5, 10)
    return ''.join(random.choice(alphabet) for _ in range(length))
