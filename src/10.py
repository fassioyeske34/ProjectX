import random

def get_random_code():
    nums = "1234567890"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    for i in range(5):
        code += random.choice(nums) + random.choice(letters)
    return code