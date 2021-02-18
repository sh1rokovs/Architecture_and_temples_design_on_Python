# Композиция vs Наследование

# Наследование
class Animal:

    def say(self):
        pass


# Кошка ЯВЛЯЕТСЯ Животным ? Да
class Cat(Animal):

    def say(self):
        pass


class Engine:

    def move(self):
        print('Move')


# Машина не является двигателем
class Car(Engine):
    pass


car = Car()
car.move()


# Композиция
# Двигатель это часть машины
class Car:

    def __init__(self, engine):
        self.engine = engine

    def change_engine(self, engine):
        self.engine = engine


engine = Engine()
car = Car(engine)

car.engine.move()
