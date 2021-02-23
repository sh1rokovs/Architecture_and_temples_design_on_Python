import abc


class Human(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self, visitor):
        pass


class Proger(Human):

    def accept(self, visitor):
        visitor.repair_car(self)


class Yurist(Human):
    def accept(self, visitor):
        visitor.repair(self)


class ConstructionElementVisitor(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def repait(self):
        pass

    @abc.abstractmethod
    def repait_car(self):
        pass


class Cool(ConstructionElementVisitor):

    @abc.abstractmethod
    def repait(self):
        print('Дорого', 'Круто')


class NotCool(ConstructionElementVisitor):

    @abc.abstractmethod
    def repait(self):
        print('Дешево', 'Не Круто')


# class Category:
#     pass
#
#
# for item in Category():
