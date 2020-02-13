# check here: https://blog.rmotr.com/python-magic-methods-and-getattr-75cf896b3f88
# also check etc/Iterator/multiply_iterator.py file also


class MagicFuncExample:
    def __init__(self, var):            # initializer
        self.var = var

    def __str__(self):                  # to provide "string representation" of your object
        """ usage: str(obj), instead of obj.__str__() """
        pass

    def __add__(self, to_be_added):     # to overload the "+" operator
        pass

    def __getattr__(self, attr):              # to catch references to attributes that do not exist in your object
        """
            Realistic example: whenever we want to provide some dynamic access to our objects.
        """
        return attr.upper()

    # def __getattribute__(self, attrr):      # Similar with __getattr__ but it intercepts EVERY attribute lookup
    #     return "hello world"

    # def __iter__(self):                 #
    #     return self
    #
    # def __next__(self):
    #     self.current = self.current + self.multiple
    #     if self.current < self.stop:
    #         return self.current
    #     else:
    #         raise StopIteration


if __name__ == "__main__":
    d = MagicFuncExample("var_x")
    # When attribute does not exist, __getattr__ is invoked.
    print(d.does_not_exist)

    # When attribute exists, __getattr__ is not invoked.
    print(d.var)

    # __getattribute__ is always invoked
    print(d.does_not_exist)
    print(d.var)
