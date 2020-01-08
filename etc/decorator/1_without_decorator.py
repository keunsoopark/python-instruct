# example from http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator/

# -*- coding: utf-8 -*-
def decorator_function(original_function):
    def wrapper_function():
        print('Before {} fn is executed.'.format(original_function.__name__))
        return original_function()

    return wrapper_function


def display_1():
    print('display_1 fn was executed.')


def display_2():
    print('display_2 fn was executed.')


display_1 = decorator_function(display_1)  # 1
display_2 = decorator_function(display_2)  # 2

display_1()
print
display_2()
