import numpy as np

def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty")
    
    average = sum(numbers) / len(numbers)
    return average

numbers = [10, 20, 30, 40, 50]
print(calculate_average(numbers))
