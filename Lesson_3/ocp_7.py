import abc


# Абстрактная фигура
class Figure(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass


# Круг
class Circle(Figure):
    def draw(self):
        pass


# Треугольник
class Triangle(Figure):
    def draw(self):
        pass


class CAD:

    # упорядоченная отрисовка
    @classmethod
    def draw_all_ordered(cls, figures):
        clone = sorted(figures, key=FigureOrderComparator.compare_order)
        cls.draw_all(clone)


class FigureOrderComparator:
    @staticmethod
    def compare_order(figure):
        return 0 if isinstance(figure, Circle) else 1
