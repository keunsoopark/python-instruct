def revert(s):
    if s:
        s = s[-1] + revert(s[:-1])
    return s


def revert_2(s):
    return s[::-1]


if __name__ == "__main__":
    str1 = "abcd"
    str2 = revert(str1)
    str3 = revert_2(str1)
    print(str2)
    print(str3)
