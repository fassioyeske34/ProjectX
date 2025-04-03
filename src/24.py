def square_root(x):
    if x < 0:
        raise ValueError("Square root of negative number not supported.")
    else:
        y = x ** (1/2)
        return y

try:
    print(square_root(-4))
except ValueError as e:
    print(e)

print(square_root(4))
