import unittest


# Прямоугольник, неизменяемый
class RectangleImmutable:
    __slots__ = ('_width', '_height')

    def __init__(self, width, height):
        super().__setattr__('_width', width)
        super().__setattr__('_height', height)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __setattr__(self, key, value):
        raise AttributeError('attributes are immutable')

    @property
    def area(self):
        return self._width * self._height


# Квадрат, неизменяемай
class SquareImmutable(RectangleImmutable):
    def __init__(self, size):
        super().__init__(size, size)


class SquareTest(unittest.TestCase):
    def test_area(self):
        rectangle = SquareImmutable(4)
        # тест пройден
        #self.assertEqual(rectangle.area, 16)

        # пытаемся изменить атрибуты
        with self.assertRaises(AttributeError):
            rectangle.width = 5

        with self.assertRaises(AttributeError):
            rectangle.width = 4
        self.assertEqual(rectangle.area, 16)
