import sys


def grep_word_from_files():
    word = sys.argv[1]
    for filename in sys.argv[2:]:
        with open(filename) as file:
            for lino, line in enumerate(file):  # so "file" is an iterable object.
                if word in line:
                    print("{0}: {1}: {2:.40}".format(filename, lino, line.rstrip()))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python-instruct {0} [word] [file ...]".format(sys.argv[0]))
        sys.exit()
    else:
        grep_word_from_files()
