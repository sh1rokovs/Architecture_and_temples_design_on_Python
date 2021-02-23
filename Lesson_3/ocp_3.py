import abc


class Figure(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass


class Circle(Figure):
    def draw(self):
        print('circle')


class Triangle(Figure):
    def draw(self):
        print('triangle')


class Romb(Figure):
    pass


romb = Romb()
print(romb.draw())
