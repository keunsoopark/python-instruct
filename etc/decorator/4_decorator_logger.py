# example from http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator/

import datetime
import time
# as using multiple decorators in one function, "wraps" provents a problem of sequential application of decorators.
from functools import wraps


# This decorator write the timestamp of orginal_function is executed in log file.
def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info('[{}] executed: args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


# This decorator shows the time consumption of executing the original_function
def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper_1(*args, **kwargs):
        t1 = time.time()
        original_function(*args, **kwargs)
        t2 = time.time() - t1
        print("Total time consumption of executing function {}: {} sec".format(original_function.__name__, t2))
        return None

    return wrapper_1


# without "wraps", my_logger decorator applies on my_timer, instead of display_info
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print("display_info({}, {}) fn was executed".format(name, age))


display_info("keunsoo", 25)
