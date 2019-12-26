# find GCD(greatest common divisor): 최대공약수


def finding_gcd(a, b):
    while b != 0:
        print(a, b)
        result = b
        a, b = b, a % b
    return result


def finding_gcd_rec(a, b):
    if a % b != 0:
        return finding_gcd_rec(b, a % b)
    else:
        return b


def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert (finding_gcd(number1, number2) == 3)
    assert (finding_gcd_rec(number1, number2) == 3)


if __name__ == "__main__":
    test_finding_gcd()
