# generate prime with n-digit (in 2 base)
# ex) insert 3 -> result is 5 (101) or 7 (111)


import math
import random
import sys


# find prime by using all possible numbers
def finding_prime(number):
    num = abs(number)
    if num < 4: return True
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def generate_prime(number=3):
    while True:
        a = pow(2, number-2) # minimum number with "number-1"-digit (ex. number=3, a=2)
        b = pow(2, number-1) # maximum number with "number-1"-digit (ex. number=3, b=4)
        p = random.randint(pow(2, number-2), pow(2, number-1)-1)
        p = 2 * p + 1
        if finding_prime(p):
            return p


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generate_prime.py number")
        sys.exit()
    else:
        number = int(sys.argv[1])
        print(generate_prime(number))

