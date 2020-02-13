# example from http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator/

# -*- coding: utf-8 -*-
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Before {} fn is executed.'.format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display_1():
    print('display_1 fn was executed.')


# function with arguments => Then there should be "*args, **kwargs" in wrapper_function()
@decorator_function
def display_info(name, age):
    print('display_info({}, {}) fn was executed'.format(name, age))


display_1()
print
display_info("keunsoo", 25)
