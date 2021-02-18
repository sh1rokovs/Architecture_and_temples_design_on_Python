import abc


class Animal(abc.ABC):

    @abc.abstractmethod
    def say(self):
        pass

    @staticmethod
    def create_animal(animal_type):
        ANIMALS = {
            'dog': Dog,
            'cat': Cat,
            'parrot': Cat
        }
        return ANIMALS[animal_type]()


class Dog(Animal):

    def say(self):
        print('wow-wow')


class Cat(Animal):

    def say(self):
        print('мяу-мяу')


class Parrot(Animal):

    def say(self):
        print('я попугай')


class AnimalCreator:

    @staticmethod
    def create_animal(animal_type):
        if animal_type == 'dog':
            animal = Dog()
        elif animal_type == 'cat':
            animal = Cat()
        elif animal_type == 'parrot':
            animal = Parrot()
        return animal


def create_animal(animal_type):
    if animal_type == 'dog':
        animal = Dog()
    elif animal_type == 'cat':
        animal = Cat()
    elif animal_type == 'parrot':
        animal = Parrot()
    return animal


ANIMALS = {
    'dog': Dog,
    'cat': Cat,
    'parrot': Cat
}
