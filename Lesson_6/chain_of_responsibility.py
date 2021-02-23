import abc
import random


class Handler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self, request):
        if self.next is not None:
            self.next.handle(request)

    def link(self, next):
        self.next = next
        return self.next


class Request:
    data = [
        'вопрос по возврату товара',
        'вопрос по скидке',
        'вопрос по стоимости товара',
        'вопрос по дефекту',
        'вопрос по новинке',
    ]

    def get_data(self):
        # return random.sample(__class__.data, 1)[0]
        return random.choice(__class__.data)


class Operator(Handler):
    # вероятность занятости оператора
    probability = 0.99

    def __init__(self, name):
        self.name = name

    def handle(self, request):
        if self.is_busy():
            print(f'Оператор {self.name} занят')
            super().handle(request)
        else:
            print(f'Оператор {self.name} обрабатывает: "{request.get_data()}"')

    def is_busy(self):
        return random.random() < __class__.probability


class BusyHandler(Handler):
    def __init__(self):
        self.request = None

    def handle(self, request):
        if (self.request == request):
            print('Все операторы заняты, пожалуйста подождите')
        else:
            self.request = request

        super().handle(request)


handler = BusyHandler()

handler.link(Operator("#1")). \
    link(Operator("#2")). \
    link(Operator("#3")). \
    link(Operator("#4")). \
    link(handler)

# генерируем поток из 3 запросов
for _ in range(3):
    handler.handle(Request())
