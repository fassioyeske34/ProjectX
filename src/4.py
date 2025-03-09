
import random

def generate_random_code(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = ""
    for i in range(length):
        code += random.choice(characters)
    return code