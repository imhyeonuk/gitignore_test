import random

def generate_random_number():
    return random.randint(1, 100)

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


number = generate_random_number()
print(number)
result = check_even_odd(number)
print(result)
