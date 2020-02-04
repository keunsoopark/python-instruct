

def else_error(filename):
    try:
        f = open(filename, "r")
    except IOError:
        print("Cannot open {0}".format(filename))
    else:
        print("{0} contains {1} lines in total.".format(filename, len(f.readline())))
        f.close()


if __name__ == "__main__":
    filename = "hello.py"
    else_error(filename)
