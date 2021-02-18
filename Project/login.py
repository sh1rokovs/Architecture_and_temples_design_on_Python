from patterns.singletone import SingletonByName
import time


class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    def logs(self, text):
        print('logs:', text)


def debug(func):
    def internal(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Debug:', func.__name__, end - start)
        return result

    return internal
