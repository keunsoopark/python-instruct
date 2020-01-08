# This examples show the Google Python guide's way of using raise error & assert together
# Principle: "assert" is used to assure the accuracy internally, rather than forcing the correct usage
# or indicating the unexceptable error occurs.


def assert_good_example(minimum):
    # Connect to the next available port. Return the minimum port
    if minimum <= 1024:
        raise ValueError("You need to provide a port larger than 1025.")    # forcing the proper usage
    port = _FindNextOpenPort(minimum)
    if not port:
        raise ConnectionError("Cannot connect %d port" % (minimum,))    # indicating unexpectable error
    assert port >= minimum, "Used an exceptable %d port. Inserted minimum port is %d." % (port, minimum)    # to increase the accuracy of "_FindNextOpenPort" func.
    return port


def assert_bad_example(minimum):
    assert minimum > 1024, "You need to provide a port larger than 1025."
    port = _FindNextOpenPort(minimum)
    assert port is not None
    return port


if __name__ == "__main__":
    minimum = 1
    assert_good_example(minimum)
    assert_bad_example(minimum)
