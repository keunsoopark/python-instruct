import sys


def read_data(filename):
    lines = []
    try:
        with open(filename) as fh:
            for line in fh:
                if line.strip():    # if there is only "\n" in line, line.strip() returns None
                    lines.append(line)
    except (IOError, OSError) as err:
        print(err)

    return lines


def write_data(lines, filename):
    try:
        with open(filename, "w") as fh:
            for line in lines:
                fh.write(line)
    except (IOError, OSError) as err:
        print(err)


def remove_blank_lines():
    if len(sys.argv) < 2:
        print("Usage: python {0} [file ...]".format(sys.argv[0]))
        sys.exit()

    for filename in sys.argv[1:]:
        lines = read_data(filename)
        if lines:
            write_data(lines, filename)


if __name__ == "__main__":
    remove_blank_lines()