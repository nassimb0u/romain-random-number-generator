import random
from converter import to_roman_numerals

def romain_randint(a, b):
    n = random.randint(a, b)
    return to_roman_numerals(n), n

if __name__ == '__main__':
    print(romain_randint(1, 4095))