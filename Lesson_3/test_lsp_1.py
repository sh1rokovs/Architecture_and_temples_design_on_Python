import unittest


# Прямоугольник
class Rectangle:
    @property
    def width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    @property
    def area(self):
        return self.__width * self.__height


# Квадрат - ?
class Square(Rectangle):
    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height):
        super().set_height(height)
        super().set_width(height)


class SquareTest(unittest.TestCase):
    def test_area(self):
        #
        rectangle = Square()
        # нарушение принципа LSP, мы не ожидаем тут, что и высота ТОЖЕ изменится
        rectangle.set_width(5)
        rectangle.set_height(4)
        # тест провален, актуальное значение 16
        self.assertEqual(rectangle.area, 20)
