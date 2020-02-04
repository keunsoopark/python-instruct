# find prime


# find prime by using all possible numbers
def finding_prime(number):
    num = abs(number)
    if num < 4: return True
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def test_finding_prime():
    number1 = 17
    number2 = 20
    assert(finding_prime(number1) is True)
    assert(finding_prime(number2) is False)


if __name__ == "__main__":
    test_finding_prime()
