from patterns.prototype import PrototypeMixin


class User:
    pass


class Administrator(User):
    pass


class SimpleFactory:
    def __init__(self, types=None):
        self.types = types or {}


class UserFactory:
    types = {
        'administrator': Administrator,
    }

    @classmethod
    def create(cls, type_):
        return cls.types[type_]()


class Category:
    increment = 0

    def __init__(self, name, category):
        self.id = Category.increment
        Category.increment += 1
        self.name = name
        self.category = category
        self.services = []

    def services_count(self):
        result = len(self.services)
        if self.category:
            result += self.category.sevices_count()
        return result


class Service(PrototypeMixin):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.services.append(self)


class RecordService(Service):
    pass


class ServiceFactory:
    types = {
        'record': RecordService
    }

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


class SiteWIthServices:
    def __init__(self):
        self.administrator = []
        self.services = []
        self.categories = []

    def create_user(self, type_):
        return UserFactory.create(type_)

    def create_category(self, name, category=None):
        return Category(name, category)

    def find_category_by_id(self, id):
        for item in self.categories:
            print('item', item.id)
            if item.id == id:
                return item
        raise Exception(f'Нет категории с id = {id}')

    def create_service(self, type_, name, category):
        return ServiceFactory.create(type_, name, category)

    def get_service(self, name) -> Service:
        for item in self.services:
            if item.name == name:
                return item
        return None
