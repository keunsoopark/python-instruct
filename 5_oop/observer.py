# How to implement getter/setter in Python with using decorators

class C:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = "{0} >> {1}".format(self._name, new_name)


if __name__ == "__main__":
    c = C("Jin")
    print(c._name)  # _name becomes "protected member" because of prefix("_")
    print(c.name)
    c.name = "Astin"
    print(c.name)
