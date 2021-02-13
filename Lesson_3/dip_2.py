import abc


# абстракция товара
class ItemInterface(abc.ABC):
    @abc.abstractmethod
    def get_price(self):
        '''returns the price'''


# превосходный  товар наследуем от абстрактного товара
class PerfectItem(ItemInterface):
    def get_price(self):
        pass


class Order:
    ...

    # добавить абстрактный товар, детали реализации товара не интересуют
    def add(self, item: ItemInterface):
        self.total += item.get_price()
