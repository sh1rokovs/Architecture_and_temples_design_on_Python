import abc


class Writer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write_message(self):
        pass


class ConcreteWriter(Writer):
    def write_message(self):
        print('writing message')


class WriterDecorator(Writer, metaclass=abc.ABCMeta):
    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def write_message(self):
        pass


class CheckLengthDecorator(WriterDecorator):
    def write_message(self):
        print('checking message length')
        self._component.write_message()


class CompressDecorator(WriterDecorator):
    def write_message(self):
        print('compressing message')
        self._component.write_message()
        print('check compressed length')


concrete_writer = ConcreteWriter()
check_length_decorator = CheckLengthDecorator(concrete_writer)
compress_decorator = CompressDecorator(check_length_decorator)
compress_decorator.write_message()


# На функциях
def old():
    print('one')


def decorator(old_f):
    def inner(*args, **kwargs):
        print('two')
        return old_f(*args, **kwargs)

    return inner


old = decorator(old)
old = decorator(old)
old = decorator(old)
old()
