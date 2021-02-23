# bad
class Order:
    def get_items(self):
        pass

    def get_total(self):
        pass

    def validate(self):
        pass

    def save(self):
        pass

    def load(self):
        pass


# good
class Order:
    def get_items(self):
        pass

    def get_total(self):
        pass

    def validate(self):
        pass


class OrderRepository:
    def save(self):
        pass

    def load(self):
        pass
