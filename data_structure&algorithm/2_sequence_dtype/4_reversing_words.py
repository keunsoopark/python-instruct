# This is my algorithm
def reversing_words_sentence_logic_kp(sentence):
    str_list = sentence.split(" ")
    str_list = str_list[::-1]
    reversed_str = " ".join(str_list)

    return reversed_str


# ----- 4_reversing_words -----
def reverser(string1, p1=0, p2=None):
    if len(string1) < 2:
        return string1
    p2 = p2 or len(string1) - 1
    while p1 < p2:
        string1[p1], string1[p2] = string1[p2], string1[p1]
        p1 += 1
        p2 -= 1


def reversing_words_sentence_logic(string1):
    # first, reverse the entire sentence
    reverser(string1)

    p = 0
    start = 0
    while p < len(string1):
        if string1[p] == u"\u0020":
            # reverse the words again
            reverser(string1, start, p - 1)
            start = p + 1
        p += 1
    # reverse the last word
    reverser(string1, start, p - 1)
    return "".join(string1)


# -----------------------------------------

# ----- 5_reversing_words -----
def reverse_words_brute(string):
    word, sentence = [], []
    for character in string:
        if character != " ":
            word.append(character)
        else:
            if word:
                sentence.append("".join(word))
            word = []
    # add the last word
    if word != "":
        sentence.append("".join(word))
    sentence.reverse()
    return " ".join(sentence)


# -----------------------------------------

# ----- 6_reversing_words -----
def reversing_words_slice(word):
    new_word = []
    words = word.split(" ")
    for word in words[::-1]:
        new_word.append(word)
    return " ".join(new_word)


# -----------------------------------------

# ----- 7_reversing_words : THIS IS THE BEST -----
def reversing_words(str1):
    words = str1.split(" ")
    rev_set = " ".join(reversed(words))
    return rev_set


def reversing_words2(str1):
    words = str1.split(" ")
    words.reverse()
    return " ".join(words)


if __name__ == "__main__":
    str1 = "Python algorithm is so fun"
    str2 = reversing_words_sentence_logic_kp(str1)
    str4 = reversing_words_sentence_logic(list(str1))
    str5 = reverse_words_brute(str1)
    str6 = reversing_words_slice(str1)
    str7_1 = reversing_words(str1)
    str7_2 = reversing_words2(str1)
    print(str2)
    print(str4)
    print(str5)
    print(str6)
    print(str7_1)
    print(str7_2)

    import timeit, functools # functools is required to pass argument to function in timeit world.

    t1 = timeit.Timer(functools.partial(reversing_words_sentence_logic_kp, str1))
    print("reversing_words_sentence_logic_kp ", t1.timeit(number=1000), "milliseconds")
    t2 = timeit.Timer(functools.partial(reversing_words_sentence_logic, list(str1)))
    print("reversing_words_sentence_logic ", t2.timeit(number=1000), "milliseconds")
    t3 = timeit.Timer(functools.partial(reverse_words_brute, str1))
    print("reverse_words_brute ", t3.timeit(number=1000), "milliseconds")
    t4 = timeit.Timer(functools.partial(reversing_words_slice, str1))
    print("reversing_words_slice ", t4.timeit(number=1000), "milliseconds")
    t5 = timeit.Timer(functools.partial(reversing_words, str1))
    print("reversing_words ", t5.timeit(number=1000), "milliseconds")
    t6 = timeit.Timer(functools.partial(reversing_words2, str1))
    print("reversing_words2 ", t6.timeit(number=1000), "milliseconds")
