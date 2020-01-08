import string
import sys


def intended_error():
    try:
        1/0 # generate ZeroDivisionError
        f = open("myfile.txt")
        s = f.readline()
        i = int(string.strip(s))
    except IOError as err:
        # errno, strerror = err.args
        print(err)
    except ValueError:
        print("Cannot convert data into number.")
    except:
        print("Error generated: {0}".format(sys.exc_info()[0]))
        raise


if __name__ == "__main__":
    intended_error()
