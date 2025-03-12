def get_random_number(max_value):
    import random
    return random.randint(0, max_value)

def main():
    print(get_random_number(10))

if __name__ == "__main__":
    main()
