# Доступ к динамическим атрибутам

class Vector:
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self.c_omponents = components

    def __getattr__(self, item):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos <= len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has not attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, key, value):
        cls = type(self)
        error = None
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'read-only attrs {attr_name!r}'
            elif name.islower():
                error = 'can\'t set attrs \'a\' to \'z\' in {cls_name!r}'
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super(Vector, self).__setattr__(name, value)
