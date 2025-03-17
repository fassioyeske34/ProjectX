def get_random_python_code():
    import random
    return "".join(chr(random.randint(97, 122)) for _ in range(50)) + "\n"
