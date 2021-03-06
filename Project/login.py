from patterns.singletone import SingletonByName
import time


class ConsoleWrite:

    def write(self, text):
        print(text)


class FileWrite:

    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, text):
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(f'{text}\n')


class Logger(metaclass=SingletonByName):

    def __init__(self, name, writer=ConsoleWrite()):
        self.name = name
        self.writer = writer

    def logs(self, text):
        text = f'log: {text}'
        self.writer.write(text)


def debug(func):
    def internal(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Debug:', func.__name__, end - start)
        return result

    return internal
