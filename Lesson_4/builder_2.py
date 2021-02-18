import abc


class TableDirector:
    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_tabletop()
        self._builder._build_legs()
        self._builder._build_coverage()


class Table:
    tabletop = 0
    legs = 0
    coverage = ''


class AbstractTableBuilder(metaclass=abc.ABCMeta):
    def __init__(self):
        self.product = Table()

    @abc.abstractmethod
    def _build_tabletop(self):
        pass

    @abc.abstractmethod
    def _build_legs(self):
        pass

    @abc.abstractmethod
    def _build_coverage(self):
        pass


class BigTableBuilder(AbstractTableBuilder):
    def _build_tabletop(self):
        self.product.tabletop = 120

    def _build_legs(self):
        self.product.legs = 4

    def _build_coverage(self):
        self.product.coverage = 'vanish'


class SmallTableBuilder(AbstractTableBuilder):
    def _build_tabletop(self):
        self.product.tabletop = 80

    def _build_legs(self):
        self.product.legs = 3

    def _build_coverage(self):
        self.product.coverage = 'yacht lacquer'


big_table__builder = BigTableBuilder()
small_table__builder = SmallTableBuilder()

director = TableDirector()
director.construct(big_table__builder)
director.construct(small_table__builder)

big_table_1 = big_table__builder.product
small_table_1 = small_table__builder.product

print(big_table_1.coverage)
print(small_table_1.coverage)
