import abc


# фигура
class Figure(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        '''draws a figure'''


# нечто печатаемое
class Plottable(abc.ABC):
    @abc.abstractmethod
    def plot(self):
        '''plots a figure'''


# круг, печатаемый - наследуемся от двух классов
class Circle(Figure, Plottable):
    def draw(self):
        print('draw Circle')

    def plot(self):
        print('plot Circle')


# направляющая, просто фигура, непечатная
class GuideLine(Figure):
    def draw(self):
        print('draw Circle')
