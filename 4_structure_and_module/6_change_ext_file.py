import sys
import os
import shutil


def change_file_ext():
    if len(sys.argv) < 2:
        print("Usage: python {0} [file ...]".format(sys.argv[0]))
        sys.exit()

    # os.path.splitext(sys.argv[1]) == sys.argv[1].split(".")
    name = os.path.splitext(sys.argv[1])[0] + "." + sys.argv[2]
    print(name)

    try:
        shutil.copyfile(sys.argv[1], name)
    except OSError as err:
        print(err)


if __name__ == "__main__":
    change_file_ext()