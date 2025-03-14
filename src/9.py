import random
def random_int(a, b):
    if a > b:
        raise ValueError("a must be less than or equal to b")
    return random.randint(a, b)

def random_float(a, b):
    if a > b:
        raise ValueError("a must be less than or equal to b")
    return random.uniform(a, b)

def random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length))

def random_date(start, end):
    if start > end:
        raise ValueError("start must be less than or equal to end")
    return random.choice(list(range(start, end+1)))

def random_bool():
    return random.choice([True, False])
