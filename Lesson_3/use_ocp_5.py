from ocp_5 import CAD, Figure


class Romb(Figure):
    def draw(self):
        print('romb')


figures = [Romb()]
CAD.draw_all(figures)
