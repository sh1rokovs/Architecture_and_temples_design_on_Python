import abc


class PriceProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_price(self, article):
        pass


class DocProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_doc(self, id):
        pass

    @abc.abstractmethod
    def send_payment(self, payment):
        pass


class MarketingProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def claim_sales(self):
        pass

    @abc.abstractmethod
    def get_bonus(self):
        pass


class ExchangeFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create__price_provider(self):
        pass

    @abc.abstractmethod
    def create__doc_provider(self):
        pass

    @abc.abstractmethod
    def create__marketing_provider(self):
        pass


class CitilinkPriceProvider(PriceProvider):
    def get_price(self, article):
        pass


class CitilinkDocProvider(DocProvider):
    def get_doc(self, id):
        pass

    def send_payment(self, payment):
        pass


class CitilinkMarketingProvider(MarketingProvider):
    def claim_sales(self):
        pass

    def get_bonus(self):
        pass


class CitilinkExchangeFactory(ExchangeFactory):
    def create__price_provider(self):
        return CitilinkPriceProvider()

    def create__doc_provider(self):
        return CitilinkDocProvider()

    def create__marketing_provider(self):
        return CitilinkMarketingProvider()


class UlmartPriceProvider(PriceProvider):
    def get_price(self, article):
        pass
        # return self.catalog.find_by_article(article).get_price()


class UlmartDocProvider(DocProvider):
    def get_doc(self, id):
        pass

    def send_payment(self, payment):
        pass


class UlmartMarketingProvider(MarketingProvider):
    def claim_sales(self):
        pass

    def get_bonus(self):
        pass


class UlmartExchangeFactory(ExchangeFactory):
    def create__price_provider(self):
        return UlmartPriceProvider()

    def create__doc_provider(self):
        return UlmartDocProvider()

    def create__marketing_provider(self):
        return UlmartMarketingProvider()


class Fabric:
    SUPPLIER_ONE = 'Citilink'
    SUPPLIER_TWO = 'Ulmart'

    # создать объект, реализующий интерфейс на основе внешней информации
    @staticmethod
    def create_factory(name):
        if name == __class__.SUPPLIER_ONE:
            return CitilinkExchangeFactory()
        elif name == __class__.SUPPLIER_TWO:
            return UlmartExchangeFactory()
        else:
            return None


def get_supplier_price(supplier_name, article):
    # создать Абстрактную фабрику сервисов конкретного поставщика
    exchange_factory = Fabric.create_factory(supplier_name)

    # создать фабрикой конкретного поставщика его провайдер некоторых услуг
    price_provider = exchange_factory.create__price_provider()

    # получить цену
    price = price_provider.get_price(article)

    return price
