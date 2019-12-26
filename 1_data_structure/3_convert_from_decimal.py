# convert a number in any base (2 < base < 10) to decimal number


def convert_from_decimal(number, to_base):
    multiplier, result = to_base, 0
    while number > 0:
        result = number % multiplier
        number = number // multiplier
        multiplier *= to_base
    return result


# def convert_from_decimal(number, to_base):
#     multiplier, result = 1, 0
#     while number > 0:
#         result = number % to_base * multiplier
#         multiplier *= 10
#         number = number // to_base
#     return result


def test_convert_from_decimal():
    number, to_base = 9, 2
    assert (convert_from_decimal(number, to_base) == 1001)


if __name__ == "__main__":
    test_convert_from_decimal()
