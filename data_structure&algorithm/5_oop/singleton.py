# singleton pattern -> only one instance for a class. Implement this by using __new__() method
## TODO: figure out how this singleton pattern works - why need to use supercalss, what __new__() does exactly etc.


class SinEx:
    _sing = None

    def __new__(cls, *args, **kwargs):
        # check if there is an instance, otherwise, create singleton instance by calling super-class
        if not cls._sing:
            cls._sing = super(SinEx, cls).__new__(cls, *args, **kwargs)
        return cls._sing


if __name__ == "__main__":
    x = SinEx()
    print(x)
    y = SinEx()
    print(y)  # y has the same address on memory with x
    print(x == y)
