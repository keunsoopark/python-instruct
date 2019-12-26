# convert decimal number to any base including lager than 10.


def convert_to_decimal_larger_bases(number, to_base):
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit = number % to_base
        result = strings[digit] + result
        number = number // to_base
    return result


def test_convert_to_decimal():
    number, to_base = 31, 16
    assert (convert_to_decimal_larger_bases(number, to_base) == "1F")


if __name__ == "__main__":
    test_convert_to_decimal()
