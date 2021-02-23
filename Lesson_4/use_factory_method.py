from factory_method import AnimalCreator, Animal, create_animal, ANIMALS

animal_type = input()
# animal = AnimalCreator.create_animal(animal_type)
animal = Animal.create_animal(animal_type)
# animal = create_animal(animal_type)
#animal = ANIMALS[animal_type]()
animal.say()
