import abc


class ConstructionElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self, visitor):
        pass


class LeverElement(ConstructionElement):
    def accept(self, visitor):
        visitor.visit_lever_element(self)


class GearElement(ConstructionElement):
    def accept(self, visitor):
        visitor.visit_gear_element(self)


class ConstructionElementVisitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visit_lever_element(self, lever_element):
        pass

    @abc.abstractmethod
    def visit_gear_element(self, gear_element):
        pass


class StrengthCalculatorVisitor(ConstructionElementVisitor):
    def visit_lever_element(self, lever_element):
        print(f'do Strength Calculation for {lever_element}')

    def visit_gear_element(self, gear_element):
        print(f'do Strength Calculation for {gear_element}')


class SpecificationCalculatorVisitor(ConstructionElementVisitor):
    def visit_lever_element(self, lever_element):
        print(f'do Specification Calculation for {lever_element}')

    def visit_gear_element(self, gear_element):
        print(f'do Specification Calculation for {gear_element}')


strength_calculator_visitor = StrengthCalculatorVisitor()
specification_calculator_visitor = SpecificationCalculatorVisitor()

lever_1 = LeverElement()
gear_1 = GearElement()


lever_1.accept(strength_calculator_visitor)
lever_1.accept(specification_calculator_visitor)

gear_1.accept(strength_calculator_visitor)
gear_1.accept(specification_calculator_visitor)
