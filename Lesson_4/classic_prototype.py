import copy


class PrototypeMixin:
    # прототип

    def clone(self):
        return copy.deepcopy(self)


class Original(PrototypeMixin):
    # __slots__ - будет ли с ним работать deepcopy?
    pass


original = Original()
original.clone()


class ModernPrototypeMixin(PrototypeMixin):

    def clone(self):
        print('что то еще')
        return copy.deepcopy(self)


class Original(ModernPrototypeMixin):
    # __slots__ - будет ли с ним работать deepcopy?
    pass


original = Original()
original.clone()
