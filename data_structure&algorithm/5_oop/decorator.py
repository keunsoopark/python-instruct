# This shows the definiton of decorator
# the following two classes are identical.


class C1(object):
    @my_decorator
    def method(self):
        pass


class C2(object):
    def method(self):
        pass

    method = my_decorator(method)   # adding additional functionalities in "my_decorator" wrapper to "method" function.


