def is_palindrome_kp(s):
    if len(s) < 2:
        return True
    if s[1] == " ":
        s = s[:1] + s[2:]
    if s[-2] == " ":
        s = s[:-2] + s[-1]
    return s[0] == s[-1] and is_palindrome_kp(s[1:-1])


def is_palindrome(s):
    # the below two lines are identical with `s2 = s2.replace(" ", "")`
    l = s.split(" ")
    s2 = "".join(l)
    return s2 == s2[::-1]


def is_palindrome2(s):
    l = len(s)
    f, b = 0, l-1
    while f < l // 2:
        while s[f] == " ":
            f += 1
        while s[b] == " ":
            b -= 1
        if s[f] != s[b]:
            return False
        f += 1
        b -= 1
    return True


def is_palindrome3(s):
    s = s.strip()  # if there are space either front or end of string, `strip` removes them.
    if len(s) < 2:
        return True
    if s[0] == s[-1]:
        return is_palindrome3(s[1:-1])
    else:
        return False


if __name__ == "__main__":
    str1 = "was it a car or a cat i saw"
    print(is_palindrome_kp(str1))
    print(is_palindrome(str1))
    print(is_palindrome2(str1))
    print(is_palindrome3(str1))

    str2 = "czuvoizjkl"
    print(is_palindrome_kp(str2))
    print(is_palindrome(str2))
    print(is_palindrome2(str2))
    print(is_palindrome3(str2))
