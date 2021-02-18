import abc


class Component(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        pass


class MachineOperation(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        print(self.name)


class CompositeOperation(Component):
    def __init__(self):
        self._child = set()

    def operation(self):
        print('folder')
        for child in self._child:
            child.operation()

    def append(self, component):
        self._child.add(component)

    def remove(self, component):
        self._child.discard(component)


# инициализация операций
operation_1 = MachineOperation('drill 5 mm')
operation_2 = MachineOperation('drill 15 mm')
composite_1 = CompositeOperation()
composite_1.append(operation_1)
composite_1.append(operation_2)

operation_3 = MachineOperation('assemble')
operation_4 = MachineOperation('paint')
composite_2 = CompositeOperation()
composite_2.append(composite_1)
composite_2.append(operation_3)
composite_2.append(operation_4)
print(composite_2._child)

# использование разных по структуре операций идентично
composite_2.operation()
# operation_1.operation()
