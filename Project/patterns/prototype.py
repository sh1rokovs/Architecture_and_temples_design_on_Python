import copy


class PrototypeMixin:

    def copy(self):
        return copy.deepcopy(self)
