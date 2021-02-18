import abc


# Абстрактная фигура
class Figure(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass


# Треугольник
class Triangle(Figure):
    def draw(self):
        pass


# решение упорядочиванием, уже лучше
class CAD:
    @classmethod
    def draw_all(cls, figures):
        for figure in figures:
            if isinstance(figure, Circle):
                figure.draw()

        for figure in figures:
            if isinstance(figure, Triangle):
                figure.draw()


class Circle(Figure):
    def draw(self):
        pass

    @staticmethod
    def compare_order(figure):
        # нарушение закрытости относительно других потомков Shape
        return 0 if isinstance(figure, Circle) else 1
