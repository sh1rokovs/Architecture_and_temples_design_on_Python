from patterns.prototype import PrototypeMixin
from patterns.observer import Subject, Observer
from orm.unit_work import DomainObject
import jsonpickle


class User:
    def __init__(self, name):
        self.name = name


class Customer(User, DomainObject):
    def __init__(self, name):
        self.services = []
        super().__init__(name)


class Administrator(User):
    pass


class SimpleFactory:
    def __init__(self, types=None):
        self.types = types or {}


class UserFactory:
    types = {
        'administrator': Administrator,
        'customer': Customer
    }

    @classmethod
    def create(cls, type_, name):
        return cls.types[type_](name)


class Category:
    increment = 0

    def __getitem__(self, item):
        return self.services[item]

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


class Service(PrototypeMixin, Subject):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.services.append(self)
        self.customer = []
        super().__init__()

    def __getitem__(self, item):
        return self.customer[item]

    def add_customer(self, customer: Customer):
        self.customer.append(customer)
        customer.services.append(self)
        self.notify()


class EmailNotifier(Observer):

    def update(self, subject: Service):
        print(('Email:', 'новый клиент', subject.customer[-1].name))


class BaseSerializer:

    def __init__(self, obj):
        self.obj = obj

    def save(self):
        return jsonpickle.dumps(self.obj)

    def load(self, data):
        return jsonpickle.loads(data)


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
        self.customer = []
        self.services = []
        self.categories = []

    def create_user(self, type_, name):
        return UserFactory.create(type_, name)

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

    def get_customer(self, name) -> Customer:
        for item in self.customer:
            if item.name == name:
                return item
