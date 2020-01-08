# difference of normal method, classmethod and statismethod

class A(object):
    _hello = True

    def foo(self, x):
        print("foo({0}, {1}) execution".format(self, x))

    @classmethod
    def class_foo(cls, x):
        print("class_foo({0}, {1}) execution: {2}".format(cls, x, cls._hello))

    @staticmethod
    def static_foo(x):
        print("static_foo({0}) execution".format(x))


if __name__ == "__main__":
    a = A()
    a.foo(1)
    a.class_foo(2)
    A.class_foo(2)
    a.static_foo(3)
    A.static_foo(3)
