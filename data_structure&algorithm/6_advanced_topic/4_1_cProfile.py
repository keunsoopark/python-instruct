import cProfile
import time


def sleep():
    time.sleep(5)


def hello_world():
    print("Hello World!")


def main():
    sleep()
    hello_world()


print(cProfile.run('main()'))

