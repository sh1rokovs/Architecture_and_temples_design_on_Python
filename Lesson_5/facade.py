class Site1Checker:
    def russian_auto(self):
        print('prices of russian cars on site 1')

    def foreign_auto(self):
        print('prices of foreign cars on site 1')


class Site2Checker:
    def russian_auto(self):
        print('prices of russian cars on site 2')

    def foreign_auto(self):
        print('prices of foreign cars on site 2')


class FacadeSiteChecker:
    def __init__(self):
        self._subsys_1 = Site1Checker()
        self._subsys_2 = Site2Checker()

    def russian_auto(self):
        self._subsys_1.russian_auto()
        self._subsys_2.russian_auto()

    def foreign_auto(self):
        self._subsys_1.foreign_auto()
        self._subsys_2.foreign_auto()


facade_site_checker = FacadeSiteChecker()
facade_site_checker.russian_auto()
facade_site_checker.foreign_auto()
