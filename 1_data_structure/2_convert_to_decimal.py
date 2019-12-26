# convert a number in any base (2 < base < 10) to decimal number


def convert_to_decimal(number, from_base):
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= from_base
        number = number // 10
    return result


def test_convert_to_decimal():
    number, from_base = 1001, 2
    assert (convert_to_decimal(number, from_base) == 9)


if __name__ == "__main__":
    test_convert_to_decimal()
