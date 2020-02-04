# convert decimal number to any base including lager than 10 with recursive function.


def convert_to_decimal_larger_bases_rec(number, to_base):
    strings = "0123456789ABCDEFGHIJ"
    if number < to_base:
        return strings[number]
    digit = number % to_base
    return convert_to_decimal_larger_bases_rec(number // to_base, to_base) + strings[digit]


def test_convert_to_decimal():
    number, to_base = 31, 16
    assert (convert_to_decimal_larger_bases_rec(number, to_base) == "1F")
    number, to_base = 9, 2
    assert (convert_to_decimal_larger_bases_rec(number, to_base) == "1001")


if __name__ == "__main__":
    test_convert_to_decimal()
