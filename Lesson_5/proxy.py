import abc


class CurrencyRateService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_currency_rate(self, currency):
        pass


class CbrCurrencyRateService(CurrencyRateService):
    def get_currency_rate(self, currency):
        # ... особенности реализации опущены
        return 0.57


class ProxyCurrencyRateService(CurrencyRateService):
    def __init__(self):
        # ссылка на реальный сервис
        self.currencyRateService = CbrCurrencyRateService()

        # кэш курсов
        self.rates = dict()


    def get_currency_rate(self, currency):
        if (currency in self.rates.keys()):
            # если курс уже имеется в кэше, выдать из кэша
            print(f'{currency}: from cache')
            return self.rates[currency]
        else:
            # если еще нет, то запросить реальный (медленный) сервис
            print(f'{currency}: from service')
            rate = self.currencyRateService.get_currency_rate(currency)
            self.rates.update({currency: rate})
            return rate



# создаем сервис
currency_rate_service = ProxyCurrencyRateService()

# получаем курс из кэша или от цб - это уже решает прокси
yen_rate_request_1 = currency_rate_service.get_currency_rate('yen')
print(yen_rate_request_1)

yen_rate_request_2 = currency_rate_service.get_currency_rate('yen')
print(yen_rate_request_2)
