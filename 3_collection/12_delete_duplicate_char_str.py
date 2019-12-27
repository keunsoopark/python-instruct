from collections import Counter
import string


def delete_unique_word_kp(str1):
    c_counter = Counter()
    for c in str1:
        c_counter[c] += 1

    unique_cs = ""
    for k, v in c_counter.items():
        if v == 1:
            unique_cs += k

    return unique_cs


def delete_unique_word(str1):
    table_c = {key: 0 for key in string.ascii_lowercase}
    for i in str1:
        table_c[i] += 1
    for key, value in table_c.items():
        if value > 1:
            str1 = str1.replace(key, "")

    return str1


def test_delete_unique_word():
    str1 = "google"
    assert(delete_unique_word_kp(str1) == "le")
    assert(delete_unique_word(str1) == "le")
    print("fib_generator passed")


if __name__ == "__main__":
    test_delete_unique_word()