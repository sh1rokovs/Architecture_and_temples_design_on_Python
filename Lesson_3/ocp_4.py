# Фигура
class Figure:
    pass


# Круг
class Circle(Figure):
    pass


# Треугольник
class Triangle(Figure):
    pass


# САПР
class CAD:
    @classmethod
    def draw_all(cls, figures):
        for figure in figures:
            # выбор поведения в зависимости от типа входного объекта
            if isinstance(figure, Circle):
                cls.draw_circle(figure)
            elif isinstance(figure, Triangle):
                cls.draw_triangle(figure)

    # рисуем круг
    @staticmethod
    def draw_circle(circle):
        pass

    # рисуем треугольник
    @staticmethod
    def draw_triangle(triangle):
        pass
