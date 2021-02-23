import abc


class PaymentStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pay(self, amount):
        pass


class PayPalPaymentStrategy(PaymentStrategy):
    # требуем учетку от paypal
    def __init__(self, email, token):
        self.email = email
        self.token = token

    def pay(self, amount):
        print(f'processing {amount} via PayPal account {self.email}')


class CreditCard:
    def __init__(self, number):
        self._number = number

    def get_number(self):
        return self._number


class CreditCardPaymentStrategy(PaymentStrategy):
    # требуется кредитка
    def __init__(self, card):
        self.card = card

    def pay(self, amount):
        print(f'processing {amount} via credit card {self.card.get_number()}')


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self._items = []

    def pay(self, strategy):
        total = self.get_total()
        strategy.pay(total)

    def get_total(self):
        total = 0
        for _item in self._items:
            total += _item.price

        return total

    def add_item(self, item):
        self._items.append(item)


# товары
item1 = Item("Book", 515)
item2 = Item("Magazine", 298)

# создаём и наполняем заказ
order = Order()
order.add_item(item1)
order.add_item(item2)

# выбор конкретной стратегии и оплата заказа
paypal_payment_strategy = PayPalPaymentStrategy("patterns@geekbrains.com", "token")
order.pay(paypal_payment_strategy)

# выбор конкретной стратегии и оплата заказа
credit_card = CreditCard("1234 5678 9101 2131 4156")
credit_card_payment_strategy = CreditCardPaymentStrategy(credit_card)
order.pay(credit_card_payment_strategy)
