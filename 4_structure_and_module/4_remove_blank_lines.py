# as you can see in 5_remove_blank_lines_with.py, using "with" is more general than using fh.close()
import sys


def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename) # default: "read" mode
        for line in fh:
            if line.strip():    # if there is only "\n" in line, line.strip() returns None
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
    finally:
        if fh:
            fh.close()

    return lines


def write_data(lines, filename):
    fh = None
    try:
        fh = open(filename, "w")
        for line in lines:
            fh.write(line)
    except (IOError, OSError) as err:
        print(err)
    finally:
        if fh:
            fh.close()


def remove_blank_lines():
    if len(sys.argv) < 2:
        print("Usage: python-instruct {0} [file ...]".format(sys.argv[0]))
        sys.exit()

    for filename in sys.argv[1:]:
        lines = read_data(filename)
        if lines:
            write_data(lines, filename)


if __name__ == "__main__":
    remove_blank_lines()