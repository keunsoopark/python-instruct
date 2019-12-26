def hello():
    print("hello")


def world():
    print("world")


functions = dict(h=hello, w=world)

action = "h"
functions[action]()
