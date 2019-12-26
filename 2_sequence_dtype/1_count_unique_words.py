# print all words in the text file in alphabetical sequence and print the counter of how many times the words are used.
# just use the code itself as text file as `python 1_counter_unique_words.py 1_counter_unique_words.py`
import string
import sys


def count_unique_word():
    words = {}
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    print("strip:", strip)
    # for filename in sys.argv[1:]:
    filename = "1_count_unique_words.py"
    with open(filename) as file:
        for line in file:
            for word in line.lower().split():  # str = "a b c"; str.split() = ["a", "b", "c"]
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] = words.get(word, 0) + 1 # dict.get(key[, value]) <- if `key` is not found, `value` is specified.

    for word in sorted(words):
        print("{0}: count {1}".format(word, words[word]))


if __name__ == "__main__":
    count_unique_word()
