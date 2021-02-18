# просто товар
class SimpleItem:
    def get_price(self):
        pass


# заказ
class Order:
    total = 0  # итого

    def add(self, item: SimpleItem):  # добавить товар в заказ
        self.total += item.get_price()


# превосходный  товар
class PerfectItem:
    def get_price(self):
        pass
