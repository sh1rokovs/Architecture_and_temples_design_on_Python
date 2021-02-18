import copy


class Original:

    # __slots__ - будет ли с ним работать deepcopy?
    pass


original = Original()
prototype = copy.deepcopy(original)

prototype.name = 2
