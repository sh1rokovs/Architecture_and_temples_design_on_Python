import abc
import math


# нечто круглое, имеющее радиус
class Roundable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_radius(self):
        pass


# окружность - имеет радиус
class Circle(Roundable):
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius


# квадрат со стороной side
class Square:
    def __init__(self, side):
        self._side = side

    def get_side(self):
        return self._side


# адаптер квадрата к круглым фигурам
class RoundableSquareAdapter(Roundable):
    def __init__(self, adaptee):
        self._adaptee = adaptee
        print(self._adaptee)

    # радиус квадрата - как радиус описанной окружности
    def get_radius(self):
        return self._adaptee.get_side() * math.sqrt(2) / 2


# создаем класс для сортировки объектов Roundable

class SortRoundable(RoundableSquareAdapter):
    def compare_order(self):
        if issubclass(self.__class__, Roundable):
            return self.get_radius()
        else:
            return RoundableSquareAdapter(self).get_radius()


# список окружностей и квадратов
figures_1 = [Circle(5), Square(5), Circle(2), Square(2)]


def compare_order(item):
    if issubclass(item.__class__, Roundable):
        return item.get_radius()
    else:
        return RoundableSquareAdapter(item).get_radius()


# отсортированный список окружностей и квадратов
ordered_figures = sorted(figures_1, key=SortRoundable.compare_order)

# выводим значения радиуса для фигур
for item in ordered_figures:
    if issubclass(item.__class__, Roundable):
        print(item.get_radius())
    else:
        print(RoundableSquareAdapter(item).get_radius())
