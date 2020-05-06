"""
    Assign a random properties in constructor
"""


class BunchClass(dict):
    def __init__(self, *args, **kwds):
        super(BunchClass, self).__init__(*args, **kwds)
        self.__dict__ = self
        """
            __dict__: it contains all the attributes which describe the object in question
            
            ex)
            def func():
                pass

            func.temp = 1

            print(func.__dict__)
            
            result: {'temp': 1}
        """


def main():
    # 1) Specialized dictionary
    bc = BunchClass
    tree = bc(left=bc(left="Buffy", right="Angel"),
              right=bc(left="Willow", right="Xander"))
    print(tree)

    # 2) Normal dictionary
    tree2 = dict(left=dict(left="Buffy", right="Angel"),
                 right=dict(left="Willow", right="Xander"))
    print(tree2)


if __name__ == "__main__":
    main()
